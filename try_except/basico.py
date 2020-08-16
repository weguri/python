"""
BaseException
    Todas exceptions herdam nesta classe
    Quando não se sabe o erro para se capturar
    pode se utilizar desta classe

    Exemplo:
        except BaseException as er:
            ou
        except:
    
    Envez de usar somente except se deveria ultilizar 
        except BaseException as er:

Pode haver varios except 
Estrutura:
    try:
        pass
    except:
        pass
    else:
        pass
    finally:
        pass
"""

try:
    print(2 / 0)
except BaseException as err:
    print("Erro:", err)
