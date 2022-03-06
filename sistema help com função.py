def ajuda(entrada):
    fim = ('\033[1;30;41mFIM')
    print('\033[1;30;46m')
    help(entrada)
print('\033[1;33;40mSistema de ajuda PYHelp')
ajuda(input('\033[mFunção ou biblioteca:'))
entrada = 0
while entrada != 'fim':
    print('\033[1;33;40mSistema de ajuda PYHelp')
    ajuda(str(input('\033[mFunção ou biblioteca:')))

