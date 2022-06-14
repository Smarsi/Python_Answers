<h1>Exercício 5</h1>

*****

<p>Para a resolução deste exercício foram criadas 3 funções. Veja abaixo o que cada uma faz: </p>

<ul>
    <li><b>Função Verifica_Validade()</b>: Recebe uma data (retirada da trilha do cartão) e compara com a data atual. Retorna se o cartão é válido ou está expirado.</li><br>
    <li><b>Função Identificador()</b>: Recebe os numeros identificadores retirados da trilha do cartão. Dentro desta função temos uma lista de bancos e seus códigos identificadores (considerei que nessa lista o último elemento sempre é o nome do banco). A função conta quantos digitos são necessários para fazer a comparação e percorre a lista verificando se os identificadores do cartão são compatíveis com os de algum banco. A função retorna o nome do banco. </li><br>
    <li><b>Função Tratamento_Cartao()</b>: Recebe a trilha do cartão e destrincha todos os dados. Essa é a função principal do programa e está chamando dentro dela as demais funções. Retorna um objeto (json) com todos os dados do cartão descritos. O resultado é igual a imagem abaixo. Também é possível ver um arquivo de resultados dentro do repositório (resultado.json)</li><br>
</ul>

![resultado_ex5_final_console](https://user-images.githubusercontent.com/38111460/173625224-5beb8ae4-b316-4eac-b9aa-202f72b0e9dc.PNG)


<br>
<br>

*****

<p>As ultimas linhas do programa estão com os dados do cartão (colocados manualmente no código), porém, em um contexto sistemico esses dados seriam recebidos por meio de uma rotina "automatizada".</p>
<br>
<p>Utilizei a biblioteca "re" do python para poder encontrar os digitos na quantidade desejada.</p>
