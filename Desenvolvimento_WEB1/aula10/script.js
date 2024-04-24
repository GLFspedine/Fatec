let adicional=0;
let entrega=0;

function calcularTotalPagar(){
    let total = 0;
    calcularAdicionais();

}

function calcularAdicionais(){
    adicional = 0;
    let selecionados;
    selecionados = document.querySelectorAll("input[name='adicional']");
    let qtd = selecionados.length;
    for (i=0; i< qtd; i++){
        if (selecionados[i].checked){
            adicional += Number(selecionados[i].value);
        }       
    }
    alert(adicional);
}

function calcularEntrega(){

}