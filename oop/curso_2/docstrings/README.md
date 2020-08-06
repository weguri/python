# Personalizar o objeto cursor
As subclasses de curso são usadas para personalizar como o resultado retornado pelo curso ou modificar o comportamento do objeto.

> Exemplo de como são herdados da classe MySQLCursor
- **MySQLCursorBuffered**
- **MySQLCursorRaw**
- **MySQLCursorBufferedRaw**
- **MySQLCursorDict**
- **MySQLCursorBufferedDict**
- **MySQLCursorNamedTuple**
- **MySQLCursorBufferedNamedTuple**
- **MySQLCursorPrepared**

### Classe MySQLCursorBuffered
- Para utilizar buffer em conjunto ao cursor, tem que passar o valor **buffered=True**.
- Também é possível realizar o buffer na conexão, isso ficar ativo para todos os cursores.