function CreateBitcoin(){
    let date = document.createElement("input")
    date.type = "date"
    date.width = "25%"
    date.id = "date"
    document.body.appendChild(date)
   
}
CreateBitcoin()

function SearchBitcoin(){
    let label = document.createElement("label")
    day =  document.querySelector("#date").valueAsDate
    br = document.createElement("br")
$.getJSON(`https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=EUR&date=${day.getFullYear() + (day.getMonth()<10 ? '0' :'') + (day.getMonth()+1) + (day.getDate()<10 ? '0':'') + day.getDate()}&json`, function(data){
    
     
    label.textContent = "EUR on current date"+"  "+data[0].rate
  });
    
    
    
    document.body.appendChild(br)
    document.body.appendChild(label)
    
    
    

    
}