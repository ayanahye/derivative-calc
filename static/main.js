var form = document.getElementById('f');
function getEquation() {
    var equation = document.getElementById('equation');
    if (equation.value) {
        alert("Hello user, please review the instructions tab if any errors. Thank you.");
    }
}

/*
const tab1 = document.getElementById('tab1');
const tab2 = document.getElementById('tab2');
const tab3 = document.getElementById('tab3');

function active(event) {
    const active = document.querySelector('.active');
    if (active) {
        active.classList.remove('active')
    }
    event.target.className = "active";
}

tab1.addEventListener('click', active.bind(this))
tab2.addEventListener('click', active.bind(this))
tab3.addEventListener('click', active.bind(this))
*/
