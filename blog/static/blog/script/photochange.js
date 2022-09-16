function photochange() {
    let form=document.getElementById('charge')
    let photo=document.getElementById('profil')
    let selecteurImage=document.getElementById('id_profil')
    
    selecteurImage.addEventListener('change',()=>{
        if (selecteurImage.files.length===0) {
            alert('choisissez une image')
        }else{
            imageContent=selecteurImage.files[0]
            photo.src=URL.createObjectURL(imageContent)

        }
            alert('changement')
        
    })
}

document.addEventListener('DOMContentLoaded',photochange)