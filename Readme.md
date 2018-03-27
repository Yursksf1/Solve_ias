# Respuestas de Prueba ias
**By: Yurley Sanchez**

En el siguiente readme se hace entrega de las soluciones propuestas a los ejercicios enunciados. 


## Problem 1 - Python
Escriba un programa en *python* que dado una lista de string tenga como salida los sigientes casos.

- alternate(["abc","123","xyz"]) => "a1xb2yc3z"
- alternate(["abc","1"]) => "a1bc"
- alternate(["abcd","1","x"]) => "a1xb2cd"
- alternate(["ab","1234"]) => "a1b234"

```python
def getValor(a,i,j):
    try:
        return a[i][j]
    except:
        return ""

def alternate(a):
    w = ''
    for i in range(0,4):
        for j in range(0,4):
            w += getValor(a,j,i)
    return w
```
### Test


```python
alternate(["abc","123","xyz"])
alternate(["abc","1"])
alternate(["abcd","12","x"])
alternate(["ab","1234"])
```


## Problem 2 - JavaScript
Escriba un programa en *Javascript* que dado una lista de string tenga como salida los siguientes casos.

- alternate(["abc","123","xyz"]) => "a1xb2yc3z"
- alternate(["abc","1"]) => "a1bc"
- alternate(["abcd","1","x"]) => "a1xb2cd"
- alternate(["ab","1234"]) => "a1b234"

```javascript
function getValor(a,i,j){
    try {
        if (a[i][j]){
            return a[i][j];
        }
        return "";
    }
    catch(err){
        return "";
    }
}

function alternate(a){
    w="";
    for(i=0; i<5; i++){
        for(j=0; j<5; j++){
            w = w + getValor(a,j,i);
        }
    }
}
```
### Test


```javascript
alternate(["abc","123","xyz"])
alternate(["abc","1"])
alternate(["abcd","12","x"])
alternate(["ab","1234"])
```

## Problem 3 - SQL
Escriba una instrucción SQL para encontraraquellas filas de la tabla *testtable* que contiene el guión bajo del carácter de escape (_) en su columna *'col1'*

- A001/DJ-402\44_/100/2015
- A001_\DJ-402\44_/100/2015
- A001_DJ-402-2014-2015
- A002_DJ-401-2014-2015
- A001/DJ-401
- A001/DJ-402\44
- A001/DJ-402\44\2015
- A001/DJ-402%45\2015/200
- A001/DJ-402\45\2015%100
- A001/DJ-402%45\2015/300
- A001/DJ-402\44

```sql
SELECT * FROM testtable WHERE col1 LIKE '%\_%' ESCAPE '\';
```

## test
```sql
SELECT * FROM testtable WHERE col1 LIKE '%\_%' ESCAPE '\';
```

| id     | col1    | 
| --------|---------|
| 1 | A001/DJ-402\44_/100/2015" |
| 2 | A001_\DJ-402\44_/100/2015" |
| 3 | A001_DJ-402-2014-2015" |
| 4 | A002_DJ-401-2014-2015" |
| 5 | A001/DJ_401" |
| 6 | A001/DJ_402\44" |
| 7 | A001/DJ_402\44\2015" |
| 9 | A001/DJ_402\45\2015%100" |
| 10 | A001/DJ_402%45\2015/300" |
