import re 

class Pessoa:

    def __init__(self, nome, idade):
        
        if type(nome) is not str:
            raise TypeError
        elif nome == "":
            raise ValueError
        
        if type(idade) is not int:
            raise TypeError
        elif idade < 0:
            raise ValueError

        self.__nome = nome
        self.__idade = idade
        
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @aniversario.setter
    def aniversario(self, idade):
        self.__idade += 1


class Funcionario(Pessoa):

    def __init__(self, nome, idade, email, carga_horaria):

        super().__init__(nome, idade)
        self.email = email
        self.carga_horaria = carga_horaria

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novo_email):

        if type(email) is str:
            
            if re.match('[\w]*@[\w]*.[\w]', email):
            
                arroba=0
                for i in email:
                    if i=='@':
                        arroba+=1
                if arroba==1:
                    print('ta certo')
                                        
                else:
                    raise ValueError
            else:
                raise ValueError
        else:
            raise TypeError


    @property
    def carga_horaria(self):
        raise NotImplementedError

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        raise NotImplementedError

    def calcula_salario(self):
        raise NotImplementedError

    def aumenta_salario(self, salario_hora):
        self.__salario_hora *= 1.05


class Programador(Funcionario):

    def __init__(self, nome, idade, email, carga_horaria):
        super().__init__(nome, idade, email, carga_horaria)
        self.__salario_hora = 35
        self.carga_horaria = carga_horaria

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        if nova_carga_horaria < 20 or nova_carga_horaria > 40:
            raise ValueError

        self.__carga_horaria = nova_carga_horaria

    def calcula_salario(self):
        return self._salario_hora * self.carga_horaria * 4.5

class Estagiario(Funcionario):

    def __init__(self, nome, idade, email, carga_horaria):
    super().__init__(nome, idade, email, carga_horaria)
    self.__salario_hora = 15.50
    self.__auxilio_alimentacao = 250.00

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        if nova_carga_horaria < 16 or carga_horaria > 30:
            raise ValueError

        self.__carga_horaria = nova_carga_horaria

    def calcula_salario(self):
        return (self._salario_hora * self.carga_horaria * 4.5 + self.__auxilio_alimentacao)
    
    
class Vendedor(Funcionario):

    def __init__(self, nome, idade, email, carga_horaria):
    super().__init__(nome, idade, email, carga_horaria)
    self.__salario_hora = 30.00
    self.__auxilio_alimentacao = 350.00
    self.__auxilio_transporte = 30.00    
    
    
    @property
    def visitas(self):
        return self.__visitas

    def realizar_visita(self, n_visitas):
        if type(n_visitas) is not int:
            raise TypeError
            
        if n_visitas < 0 and n_visitas > 10:
            raise ValueError
            
        self.__visitas += n_visitas
            

    def zerar_visitas(self):
        self.__visitas = 0
    
    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        if nova_carga_horaria < 15 or carga_horaria > 45:
            raise ValueError

        self.__carga_horaria = nova_carga_horaria

    def calcula_salario(self):
        return ((self._salario_hora * self.carga_horaria * 4.5)
            + self.__auxilio_alimentacao + 
            (self.__visitas * self.__auxilio_transporte))
    


class EmpresaCreationError(Exception):
    pass


class Empresa:

    def __init__(self, nome, cnpj, area_atuacao, equipe):
 
        self.nome = nome
        self.cnpj = cnpj
        self.area_atuacao = area_atuacao
        self.__equipe = []
        
        try:
            for i in equipe:
                self.contrata(i)
        except TypeError:
            raise EmpresaCreationError
            
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if type(nome) is not str:
            raise EmpresaCreationError

        self.__nome = novo_nome

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, novo_cnpj):
        if type(cnpj) is not str:
            raise EmpresaCreationError

        self.__cnpj = novo_cnpj

    @property
    def area_atuacao(self):
        return self.__area_atuacao

    @area_atuacao.setter
    def area_atuacao(self, nova_area_atuacao):
        if type(nova_area_atuacao) is not str:
            raise EmpresaCreationError

        self.__area_atuacao = nova_area_atuacao
            

    @property
    def equipe(self):
        return self.__equipe

    def contrata(self, novo_funcionario):
        if not isinstance(novo_funcionario, Funcionario):
            raise TypeError
        
        self.__equipe.append(novo_funcionario)

    def folha_pagamento(self):
        return sum([i.calcula_salario() for i in self.equipe])
        

    def dissidio_anual(self):
        for i in self.equipe:
            i.aumenta_salario()

    def listar_visitas(self):
        return {i.email : i.visitas for i in self.equipe
            if isinstance(i, Vendedor)}

    def zerar_visitas_vendedores(self):
        for i in self.equipe:
            if isinstance(i, Vendedor):
                i.zerar_visitas()
