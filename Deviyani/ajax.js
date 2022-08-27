console.log("I'm in...")


let fetchBtn = document.getElementById('fetchBtn');
fetchBtn.addEventListener('click',buttonClickHandler)

function buttonClickHandler(){

    console.log('Button been clicked')
    const xhr = new XMLHttpRequest();
    xhr.open('GET','ajax.json',true)
    console.log('Data fetched')

    xhr.onload = function(){
        console.log(this.responseText)
    }
    xhr.send();
    // fetch("ajax.json")
    // .then((res)=>{
    //     console.log(res)
    // })
    // .catch((e)=>{
    //     console.log(e)
    // })
    // xhr.send();
}