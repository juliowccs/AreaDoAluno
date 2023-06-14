function opendashboard() {
    window.open("../../dashboard.html");
}

var button = document.getElementById("areadoaluno");
button.addEventListener("click", opendashboard);

function setProgress(progress) {
    const progressBar = document.querySelector('.progress-chart-progress');
    const progressText = document.querySelector('.progress-chart-text');
  
    progressBar.style.transform = `rotate(${progress * 3.6}deg)`;
    progressText.textContent = `${progress}%`;
  }
