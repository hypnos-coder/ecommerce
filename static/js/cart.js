let updatebtns=document.getElementsByClassName('update-cart')

for (let i = 0; i < updatebtns.length; i++) {
        updatebtns[i].addEventListener('click',function(e){
        let productId=this.dataset.product
        let action=this.dataset.action
        console.log('productId:',productId,'action: ',action)

        console.log('user:',user)
        if (user=='AnonymousUser') {
            
        } else {
            updateUserOrder(productId,action)    
        }

    });
    
}
function updateUserOrder(productId, action) {
    console.log('user in')
    let url='/update-item/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringify({'productId':productId,'action':action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data:',data)
        location.reload()
    })
    
    
}