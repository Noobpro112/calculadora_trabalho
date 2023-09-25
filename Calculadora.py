equacao=str(input('Qual sua equação?'))
if equacao == 'Mais' or '+' or 'mais' :
    n1=float(input('Qual seu primeiro numero?'))
    n2=float(input('Qual seu segundo numero?'))
    total=n1+n2
    print('Seu resultado é {}'.format(total))
elif equacao== 'Menos' or '-' or 'menos':
    n1=float(input('Qual seu primeiro numero?'))
    n2=float(input('Qual seu segundo numero?'))
    total = n1-n2
    print ('O resultado da subtração entre {} e {} é igual a:'.format (n1,n2), total)
elif equacao == 'Divisão' or '/' or 'divisão' :
    n1=float(input('Qual seu primeiro numero?'))
    n2= float(input('Qual o segundo número ? '))
    total=n1/n2
    print('A divisão de {} por {} resulta em {:.3f}'. format(n1 , n2 , total ))
elif equacao== 'Multiplicação' or '*' or 'multiplicação' :
    n1=float(input('Qual seu primeiro numero?'))
    n2=float(input('Qual seu segundo numero?'))
    print('O produto do valor digitado é', n1*n2 )
elif equacao == 'Exponenciação' or 'Exponencial' or '**' :
    n1=float(input('Qual seu primeiro numero?'))
    n2=float(input('Qual seu segundo numero?'))
    print('{} elevado à potência de {} é igual a:{} '.format(n1,n2,(n1)**(n2)))
else :
    print('Opção inválida')
