
var posicionArray=[];
var time = 0;
var elementosSelect = [];
var secciones;

var boton;

window.addEventListener('mousemove', async e=>{
    let position = {
        x: e.offsetX,
        y: e.offsetY
    }

    posicionArray.push(position);
});

window.addEventListener('scroll',e=>{ 
    
});

document.addEventListener('DOMContentLoaded',()=>{
    var posicionArray=[];
    var time = 0;
    var elementosSelect = [];
    var secciones;
  
    var boton;
    let interval = setInterval(()=>{
        time++;
    },1000)

    function setDato(dato){
      console.log(dato)
    }

    boton = document.getElementById('clic');
    inputs = Array.from(document.getElementsByClassName('input'));
    console.log(inputs);
    inputs.forEach(element => {
        element.onclick = e =>{
          elementosSelect.push(e.target.name)
        }
    });

    boton.onclick = e =>{
        e.preventDefault();
        console.log(time);
        console.log(elementosSelect);
        console.log(posicionArray)
    }
});

window.addEventListener('unload', e =>{
    /*fetch('http://127.0.0.1:5000/registros/almacenaVistas',{
        'method': 'POST',
        headers:{
          'Content-Type':'application/json'
        },
        body:JSON.stringify({
          idLanding,
          time,
          date
        })
      }).then(res => res.json)
      .then(data=>console.log(data))
      .catch(err=>console.log(err));

      fetch('http://127.0.0.1:5000/registros/almacenaClic',{
        'method': 'POST',
        headers:{
          'Content-Type':'application/json'
        },
        body:JSON.stringify({
          idLanding,
          elementosSelect,
          date
        })
      }).then(res => res.json)
      .then(data=>console.log(data))
      .catch(err=>console.log(err));*/
});


const setSecciones = secciones =>{
    secciones=secciones;
}




