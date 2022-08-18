var btc = document.getElementById("bitcoin");
var eth = document.getElementById("ethereum");
var doge = document.getElementById("dogecoin");
var xrp = document.getElementById("ripple")
var ape = document.getElementById("apecoin");
var ave = document.getElementById("aave");
var link = document.getElementById("chainlink");
var uni = document.getElementById("uniswap");


var settings = {
    "async": true,
    "scrossDomain": true,
    "url": "https://api.coingecko.com/api/v3/coins/markets?vs_currency=cad&order=market_cap_desc&per_page=100&page=1&sparkline=true",
    "method": "GET",
    "headers": {}

}
$.ajax(settings).done(function(response){
    btc.innerHTML= response.bitcoin.cad;
    eth.innerHTML= response.ethereum.cad;
    doge.innerHTML= response.dogecoin.cad;
    xrp.innerHTML = response.ripple.cad;
    ape.innerHTML = response.apecoin.cad;
    ave.innerHTML = response.aave.cad;
    link.innerHTML = response.chainlink.cad;
    uni.innerHTML = response.uniswap.cad;
});

// Crypto Table
let sortDirection = false;
let cryptoData = [
    {name:'Bitcoin', price: '$30000'},
    {name:'Ethereum', price: '$2000'},
    {name:'Ripple', price: '$0.48'},
    {name:'Doge', price: '$0.10'}
];

window.onload =() => {
    loadTableData(cryptoData);
}

function loadTableData(cryptoData){
    const tableBody = document.getElementById('tableData');
    let dataHtml = '';

    for(let crypto of cryptoData){
        dataHtml += `<tr><td>${crypto.name}</td><td>${crypto.price}</td><td>${crypto.change1h}</td><td>${crypto.change24h}</td><td>${crypto.change7d}</td><td>${crypto.marketcap}</td><td>${crypto.last7days}</td></tr>`;
    }

    tableBody.innerHTML = dataHtml;
}
