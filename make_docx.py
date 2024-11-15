from tools import (findingTheSampleByTheMean,
                   checkingTheSamplesForErrors,
                   findingTheAverage,
                   findingStandardDeviation,
                   randomError,
                   fullErrorOfTheResult,
                   relativeError,
                   answerInStandardForm)
from numpy import format_float_positional
from docxtpl import DocxTemplate
from math import log10, floor
from os import path, remove


def round_to_4_significant(x):
    try:
        return round(x, -int(floor(log10(abs(x))) - 3))
    except ValueError:
        return 0


def num_to_str(x):
    return format_float_positional(x).replace('.', ',')


def makeDocument(s: list):
    s.sort()
    file = DocxTemplate('Template.docx')
    v = {
        3: 1.15,
        4: 1.46,
        5: 1.67,
        6: 1.82,
        7: 1.94,
        8: 2.03,
        9: 2.11,
        10: 2.18,
        11: 2.23,
        12: 2.29
    }
    t = {
        2: 12.7,
        3: 4.3,
        4: 3.2,
        5: 2.8,
        6: 2.6,
        7: 2.5,
        8: 2.4,
        9: 2.3,
        10: 2.3,
        100: 2.0,
    }
    context = {
        'N': len(s),
        'N-1': len(s) - 1,
        'indexes': [*range(1, len(s) + 1)],
        'sampling': [num_to_str(sample) for sample in s],
        'averagesum': ' + '.join([num_to_str(sample) for sample in s]),
        'skoelements': []
    }
    try:
        context['V'] = v[len(s)]
    except KeyError:
        raise ValueError('Невозможно провести проверку на промахи с помощью СКО. Выборка должна содержать от 3 до 12 элементов.')
    try:
        context['t'] = t[len(s)]
    except:
        raise ValueError('Невозможно вывести случайную погрешность с помощью коэффициентов Стьюдента. Выборка должна содержать от 2 до 10 элементов.')
    context['average'] = average = round_to_4_significant(findingTheAverage(s))
    context['variable'] = variable = input('Введите символ, которым обозначается введённые значения: ')
    instrumenterror = float(input('Введите приборную погрешность: ').replace(',', '.'))
    skosum = 0
    for index, value in enumerate(s, 1):
        skosum += (s[index-1] - average) ** 2
        context['skoelements'].append({
            'index': index,
            'absmidvalue': num_to_str(round_to_4_significant(abs(s[index-1] - average))),
            'midvalue': num_to_str(round_to_4_significant(s[index-1] - average)),
            'value': num_to_str(round_to_4_significant((s[index-1] - average) ** 2))})
    skomiss = v[len(s)] * (skosum / (len(s) - 1)) ** 0.5
    context['sko'] = num_to_str(round_to_4_significant((skosum / (len(s) - 1)) ** 0.5))
    context['skomiss'] = num_to_str(round_to_4_significant(skomiss))
    context['skosum'] = num_to_str(round_to_4_significant(skosum))
    context['skos'] = num_to_str(round_to_4_significant(findingStandardDeviation(s)))
    context['nomisses'] = True if all((s[0] - average < skomiss, s[-1] - average < skomiss)) else False
    context['randomerror'] = num_to_str(round_to_4_significant(randomError(s)))
    context['instrumenterror'] = num_to_str(instrumenterror)
    context['fullerror'] = num_to_str(round_to_4_significant(fullErrorOfTheResult(s, instrumenterror)))
    context['relativeerror'] = num_to_str(round(fullErrorOfTheResult(s, instrumenterror) / average * 100, 1))
    context['answer'], context['answererror'] = answerInStandardForm(s, instrumenterror)
    file.render(context)
    if path.exists('{}.docx'.format(variable)):
        remove('{}.docx'.format(variable))
    file.save('{}.docx'.format(variable))
    print('Результат сохранён в файле {}.docx'.format(variable))