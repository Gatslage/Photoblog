
function ajoutDeClasse(){
    let mesForm=document.getElementsByClassName('myform')
    for (let j = 0; j < mesForm.length; j++) {
        let monForm = mesForm[j];
        let mesEnf=monForm.children
        for (let i = 0; i < mesEnf.length; i++) {
            let monEnf = mesEnf[i];
            monEnf.classList.add('en-form')
            minis=monEnf.children
            for (let u = 0; u < minis.length; u++) {
                let mini = minis[u];
                mini.classList.add('mini-form')
            }
    }

}
}
document.addEventListener('DOMContentLoaded',ajoutDeClasse)
