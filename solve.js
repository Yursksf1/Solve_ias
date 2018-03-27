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