# Empresa-OOP-
# Learning about Object Oriented Programming

# Etapa 1 - Classe pessoa
"""
    Expõe apenas para leitura os atributos públicos:
    + nome
    + idade

    e o método público:
    + aniversario()

    --> O nome e a idade da pessoa devem ser recebidos na inicialização
        do objeto e guardados em atributos não públicos.
        * Se nome não for string, levanta um TypeError
        * Se nome for vazio, levanta um ValueError
        * Se idade não for um inteiro, levanta um TypeError
        * Se idade for negativo, levanta um ValueError

    --> A exposição (pública) do nome e da idade deve ser feita através
        de properties, sem setter.

    --> O método aniversário não recebe nenhum argumento e incrementa
        o valor da idade em +1.
    """
    
    # Etapa 2 - Classe funcionario
    
    """
    Expõe os atributos públicos:
    + email
    + carga_horaria

    E os métodos públicos:
    + calcula_salario()
    + aumenta_salario()

    Métodos (ou properties/setters) que tenham exatamente a mesma
    implementação em todas as classes filhas podem ser editados nesta classe,
    enquanto métodos (ou properties/setters) que tenham uma implementação
    específica devem ser editados nas classes filhas. Lembrando que se for
    necessário sobrescrever um setter, é necessário sobrescrever também a
    property relacionada.

    Exemplos:
    * a property/setter de email podem ser implementados nesta classe,
      pois a implementação não depende do subtipo de funcionários.
    * já a property/setter de carga_horaria deverão ser sobrescritos em cada
      uma das subclasses, pois as regras de validade da carga horária dependem
      do subtipo de funcionário.
    * aumenta_salario() terá a mesma implementação em todas as subclasses,
      pois o dissídio é de 5% sobre o valor da hora para todos os funcionários.
    * calcula_salario() terá uma implementação específica para cada tipo,
      pois dependendo da classe de funcionário, o cálculo segue regras diferentes.

      ATENÇÃO: Esta classe está simulando uma classe abstrata. Em Python isso pode
      ser feito herdando de uma classe chamada ABC, e métodos abstrados podem
      ser decorados com @abstractmethod. No entanto, isso não será cobrado nesta
      atividade e o comportamento está sendo simulado com o erro NotImplementedError,
      pois, caso o método não seja sobrescrito, uma chamada a ele irá levantar um
      erro informando que ele não foi devidamente implementado na classe filha.
      Essa classe não precisa implementar todos os métodos pois uma classe ser abstrata
      significa que ela não terá objetos criados diretamente a partir dela, servindo
      apenas de base para outras classes filhas, que essas sim terão objetos instanciados.

      tl;dr: implementem aqui os métodos com 'pass' e deixem os métodos com 'raise'
      como estão, pois eles serão sobrescritos (implementados) nas classes filhas.
    """
    
    # Etapa 3 - Funcionario
    
    """
        Construtor da classe Funcionário - lembre-se de usar o super para acessar
        o construtor da classe mãe e criar atributos que já estão definidos lá.
        Para o email e a carga horária, usem a property/setter aqui.

        O valor de carga_horaria é referente ao número de horas trabalhadas por semana
    """
    
    # Etapa 4 - email
    
    """
        Retorna email do funcionário
    """
    
    # Etapa 5 - email.setter
    
    """
        Regras de validação:
        - Deve ser uma string, senão levanta um TypeError
        - Deve conter apenas letras, números, pontos e
          exatamente 1 símbolo @, senão levanta um ValueError.
    """
    
    # Etapa 6 - carga_horaria
    """
        Retorna a carga horária semanal de trabalho do funcionário.

        (não implementar aqui)
    """
    
    # Etapa 7 - carga_horaria.setter
    """
        altera a carga horária do funcionário, respeitando o limite de horas por categoria.
        Caso o numero informado seja inválido, de acordo com o cargo, levanta um ValueError
        - Este método não possui retorno.

        (não implementar aqui)
        
     """
     
     # Etapa 8 - salario
     """
        Calcula e retorna o salário do mês para o funcionário.
     """
      
     # Etapa 9 - aumenta_salario
     """
        Aplica um aumento de 5% no valor da hora trabalhada para o funcionário
        - Este método não possui retorno;
     """
     
     """
DICAS:

Se uma classe não possui um método definido, mas este método é definido em
alguma classe mãe acima, a classe irá herdar e usar tal método exatamente como
ele está definido na classe acima.

Isto também se aplica ao construtor, se Programador não define um __init__, então
esta classe está automaticamente usando o __init__ da classe Funcionário (se
funcionário tampouco definisse um __init__, então seria usado o de Pessoa, e se
pessoa tampouco o fizesse, seria usado o de `object`, que é a classe base do Python
herdada automaticamente por todas as classes que criamos, para garantir que tenham
os métodos básicos que se espera de um objeto em Python).

Caso você queira ou precise adicionar atributos extras na classe Programador
(ou qualquer outra classe filha de Funcionário), defina o método construtor,
faça a utilização do super e adicione os atributos extra que serão específicos
daquela classe, sejam eles recebidos por parâmetros ou não.

Lembrando que o enunciado define quais são os parâmetros obrigatórios
de uma classe, então se forem criados parâmetros obrigatórios extras, isso
irá gerar erros nos testes de correção.
"""

    # Etapa 10 - Programador_Funcionario
    """
    Funcionário do tipo Programador:
    - não recebe nenhum parâmetro extra;
    - salario base por hora: R$ 35.00;
    - regime de trabalho permitido: de 20h a 40h semanais (inclusive),
      caso contrário levanta um ValueError;
    - cálculo do sálario mensal, considere:
        * número de horas trabalhadas na semana;
        * sálario base (por hora);
        * o mês possui 4.5 semanas para efeitos desse cálculo.
    """
    
    # Etapa 11 - Estagiario_Funcionário
    
    """
    Funcionário do tipo Estagiario:
    - não recebe nenhum parâmetro extra;
    - salario base por hora: R$ 15.50;
    - auxilio alimentação mensal: R$ de 250.00;
    - regime de trabalho permitido: de 16h a 30h semanais (inclusive),
      caso contrário levanta um ValueError;
    - cálculo do sálario mensal, considere:
        * número de horas trabalhadas na semana;
        * sálario base (por hora);
        * o mês possui 4.5 semanas para efeitos desse cálculo;
        * auxílio alimentação mensal fixo;
    """
    
    # Etapa 12 - Vendedor_Funcionário
    
    """
    Funcionário do tipo Vendedor:
    - não recebe nenhum parâmetro extra;

    - além dos métodos e atributos de Funcionário, deve:
      expor o atributo público, acessível apenas para leitura:
      + visitas
      e os métodos públicos:
      + realizar_visita()
      + zerar_visitas()

    - deve possuir um atributo não público que guarda o número de visitas
      realizadas no mês, começando sempre em zero no momento da criação do
      objeto. Esse atributo deve ser exposto publicamente pelo atributo `visitas`

    - salario base por hora: R$ 30.00;
    - auxilio alimentação mensal: R$ 350.00;
    - auxilio transporte por visita realizada: R$ 30.00;
    - regime de trabalho permitido: de 15h a 45h semanais (inclusive),
      caso contrário levanta um ValueError;

    - cálculo do sálario mensal, considere:
        * número de horas trabalhadas na semana;
        * sálario base (por hora);
        * o mês possui 4.5 semanas para efeitos desse cálculo;
        * auxílio alimentação mensal fixo;
        * auxilio transporte mensal variável, em função do número de visitas;
    """
    
    # Etapa 13 - visitas
     """
        Retorna o número de visitas realizadas pelo vendedor até o momento
     """
     
     # Etapa 14 - realizar_visitas
     """
        Recebe um número inteiro e incrementa o número de visitas realizadas no mês
        com o valor recebido. Antes de fazer a alteração, verifique:
        * se n_visitas é um número inteiro e levante um TypeError caso contrário;
        * se n_visitas está no intervalo de 0 a 10 (inclusive), levantando um ValueError caso contrário.

        - Este método não possui retorno;
       """
       
       # Etapa 15 - zerar visita
        """
        Quando chamado deve redefinir o número de visitas realizadas pelo vendedor para zero,
        de modo a começar a contagem para o mês seguinte.
        - Este método não possui retorno;
        """
        
        # Etapa 16 - Empresa
        
       """
    Classe empresa, gerencia diversos funcionários

    Expõe os atributos públicos:
    + nome
    + cnpj
    + area_atuacao
    + equipe

    e os métodos públicos:
    + contrata()
    + folha_pagamento()
    + dissidio_anual()
    + listar_visitas()
    + zerar_visitas_vendedores()

    """
    
            """
        Construtor da classe empresa
        - nome, cnpj e area_atuação são strings
        - equipe é uma lista de funcionários (que podem ser de qualquer subtipo)
          e deve ser guardada em um atributo não público acessível apenas para leitura
          pelo atributo público `equipe`

        - Verifique as condições acima, isto é, se os parâmetros nome, cnpj e
          area_atuação são strings e se a lista de objetos passada no parâmetro equipe
          contem apenas objetos de algum tipo de funcionário. Caso ocorra qualquer
          problema na criação da empresa, devido a essas verificações, levante um
          EmpresaCreationError.

        DICA: a verificação da lista de funcionários pode ser feita usando o método
        público `contrata` e tratando para TypeError em um bloco try-except, e levantando
        o erro adequado.
        """
        
        # Etapa 17 - equipe
        """
        Retorna a lista com todos os funcionarios da empresa
        """
        
        # Etapa 18 - contrata
        """
        Contrata um novo funcionário para a empresa (adicionando ele à lista de funcionários)

        - Verifica se novo_funcionario é um objeto de um dos subtipos de Funcionario,
          caso contrário levanta um TypeError

        DICA: Essa verificação pode ser feita usando o método isinstance(obj, cls) do Python,
        com a classe Funcionario, pois todas os objetos de uma subclasse de Funcionario também
        serão considerados instâncias de Funcionario.

        - Este método não possui retorno;
        """
        
        # Etapa 19 - folha_pagamento
        
        """
        Retorna o valor total gasto com o pagamento de todos os funcionários
        para o mês vigente

        DICA: Itere sobre a lista de funcionários, fazendo cada objeto do tipo
        Funcionário calcular seu próprio salário, acumule e retorne o resultado.
        """
        
        # Etapa 20 - dissidio
        
       """
        Aumenta o salário base por hora trabalhada com o dissídio padrão
        para todos os funcionários da empresa.
        - Este método não possui retorno;

        DICA: idem ao método de folha de pagamento, percorra a lista de funcionários e
        faça cada objeto funcionário aumentar o próprio salário base por hora.
        """
        
        # Etapa 21 - listar_visitas
        """
        Retorna um dicionário com as visitas realizadas por cada vendedor;
        Como a chave do dicionário precisa ser única, deve ser usado o email do vendedor
        e o valor deve ser o número de visitas realizadas por aquele funcionário.
        Exemplo:
            {
                'email_vendedor_1@email.ocm': <número de visitas aqui>,
                'email_vendedor_2@email.ocm': <número de visitas aqui>,
                'email_vendedor_3@email.ocm': <número de visitas aqui>
            }

        DICA: percorra a lista de funcionários e use a função `isinstance()` para verificar se
        o funcionário é um vendedor, em caso positivo, adicione as informações pedidas
        ao dicionário, e por fim retorne esse dicionário (não precisa guardar em um atributo).
        """
        
        # Etapa 22 - zerar_visitas_vendedores
        """
        Zera as visitas de todos os funcionário, use a dica do método listar_visitas e
        para cada vendedor, chame o método de zerar visitas do vendedor.
        - Este método não possui retorno;
        """
    
    
        

        
