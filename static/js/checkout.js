var shipping='{{order.shipping}}'
if(shipping=='False'){
    document.getElementById('shipping-info').innerHTML=''
}

if (user!='AnonymousUser') {
    document.getElementById('user-info').innerHTML=''
}
if (shipping=='False' && user!='AnonymousUser') {
    document.getElementById('form-wrapper').classList.add('hidden')
    document.getElementById('payement-info').classList.remove('hidden')
}

var form=document.getElementById('form')
form.addEventListener('submit',function(e){
    e.preventDefault()
    console.log('form submited')
    document.getElementById('form-button').classList.add('hidden')
    document.getElementById('payement-info').classList.remove('hidden')
})
document.getElementById('make-payement').addEventListener('click',function(e){
    submitFormdata()
})
function submitFormdata(){
    console.log('payement button clicked')
}
