import PySimpleGUI as sg

sg.theme('DarkBrown')
frame_layout = [[sg.Output(size=(30, 10), background_color='white', text_color='black')]
                ]

coluna = [[sg.Sizer(0, 20)],
          [sg.Text('Mês:',
                   size=(12, 1),
                   font=("ubunto", 10)),
           sg.Input(key='-MES-',
                    font=("ubunto", 10),
                    size=(30, 1),
                    text_color='white',
                    do_not_clear=False,
                    default_text='Ex: Janeiro')],
          [sg.Text('Funcionário:',
                   size=(12, 1),
                   font=("ubunto", 10)),
           sg.Input(key='-FUNCIONARIO-',
                    font=("ubunto", 10),
                    size=(30, 1),
                    text_color='white',
                    do_not_clear=False)],
          [sg.Text('Salário: ',
                   size=(12, 1),
                   font=("ubunto", 10)),
           sg.Input(key='-SALARIO-',
                    font=("ubunto", 10),
                    size=(30, 1),
                    text_color='white',
                    do_not_clear=False)],
          [sg.Text('Horas 50%:',
                   size=(12, 1),
                   font=("ubunto", 10)),
           sg.Input(key='-HORAS1-',
                    size=(30, 1),
                    font=("ubunto", 10),
                    text_color='white',
                    do_not_clear=False)],
          [sg.Text('Horas 100% : ',
                   size=(12, 1),
                   font=("ubunto", 10)),
           sg.Input(key='-HORAS2-',
                    size=(30, 1),
                    font=("ubunto", 10),
                    text_color='white',
                    do_not_clear=False)],
          [sg.Sizer(0, 25)]
          ]
frame_coluna = coluna

layout = [[sg.Frame('Dados', frame_coluna, vertical_alignment='top'), sg.Frame('Resultado', frame_layout)],
          [sg.Button('Entrar'), sg.Button('Salvar')]
          ]

window = sg.Window("Calculo De Horas Extras", layout=layout)


def calculo_extra_50(x_por_cento=0.0, salario=1237.00):
    """
    função para calcular horas extras 50%.
    :param x_por_cento: entrada referente as horas trabalhas do usuario em 50%.
    :param salario: entrada referente ao salario bruto do usuario.
    :return: x_por_cento * o salario / 220.00 * 0,5 * 3.
    """
    entrada1 = float(x_por_cento)
    entrada2 = float(salario)
    if entrada1 >= 0:
        valor_extra = entrada1 * round(((entrada2 / 220.00) * 0.5) * 3, 1)
        return f'Horas 50%: {valor_extra}'


def calculo_extra_100(x_por_cento=0.0, salario=1237.00):
    """
    Funçao para calcular as horas extras em 100%.
    :param x_por_cento: entrada referente as horas trabalhas do usuario em 100%.
    :param salario: Entrada referente ao salario bruto do usuario.
    :return: x_por_cento * o salario / 220.00 * 2.
    """
    entrada1 = int(x_por_cento)
    entrada2 = float(salario)
    if entrada1 >= 0:
        valor_extra = entrada1 * round((entrada2 / 220.00) * 2, 1)
        return f'Horas 100%: {valor_extra}'


while True:
    eventos, valor = window.Read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        data = valor['-MES-']
        funcionarios = valor['-FUNCIONARIO-']
        salario = float(valor['-SALARIO-'])
        horas_50 = valor['-HORAS1-']
        horas_100 = valor['-HORAS2-']
        mes = f'Mês: {str(data)}'
        nome = f'Funcionário: {funcionarios}'
        valor_50 = calculo_extra_50(horas_50, salario)
        valor_100 = calculo_extra_100(horas_100, salario)
        print(funcionarios)
        print(valor_50)
        print(valor_100)
    if eventos == 'Salvar':
        # Este arquivo salva os dados do output, cada vez que foi clicado em salavar.
        # Obs: o arquivo estara sempre acrescentando dados, mesmo depois do programa ser reinicializado.
        with open('dados.txt', 'a') as arquivo:
            while True:
                titulo = 'Dados do Usúario'
                if titulo != sg.WINDOW_CLOSED:
                    arquivo.write('\n')
                    arquivo.write(titulo.upper())
                    arquivo.write('\n')
                    arquivo.write('\n')
                    arquivo.write(mes.upper())
                    arquivo.write('\n')
                    arquivo.write(nome.title())
                    arquivo.write('\n')
                    arquivo.write(valor_50)
                    arquivo.write('\n')
                    arquivo.write(valor_100)
                    arquivo.write('\n')
                    break
