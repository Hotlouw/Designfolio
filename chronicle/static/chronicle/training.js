
let currentIndex = 0;
	
function showSlide(index) {
  const slider = document.querySelector('.slider');
  const slideWidth = document.querySelector('.slide').offsetWidth;
  const newPosition = -index * slideWidth;
  slider.style.transform = `translateX(${newPosition}px)`;
}

function prevSlide() {
  currentIndex = (currentIndex - 1 + 7) % 7; // Adjust the number based on the total number of slides
  showSlide(currentIndex);
}

function nextSlide() {
  currentIndex = (currentIndex + 1) % 7; // Adjust the number based on the total number of slides
  showSlide(currentIndex);
}

// Auto-slide every 1 second
setInterval(() => {
  nextSlide();
}, 3000);


  function scrollToContentfreecodecamp() {
      const contentElement = document.getElementById('contentfreecodecamp');
      contentElement.scrollIntoView({ behavior: 'smooth' });}

  function scrollToContentlinkedin() {
      const contentElement = document.getElementById('contentlinkedin');
      contentElement.scrollIntoView({ behavior: 'smooth' });}

  function scrollToContentmedium() {
      const contentElement = document.getElementById('contentmedium');
      contentElement.scrollIntoView({ behavior: 'smooth' });}			

  function scrollToContentrealpython() {
      const contentElement = document.getElementById('contentrealpython');
      contentElement.scrollIntoView({ behavior: 'smooth' });}

  function scrollToContentudemy() {
      const contentElement = document.getElementById('contentudemy');
      contentElement.scrollIntoView({ behavior: 'smooth' });}

  function scrollToContentyoutube() {
      const contentElement = document.getElementById('contentyoutube');
      contentElement.scrollIntoView({ behavior: 'smooth' });}
      
  function scrollToContentwebflow() {
      const contentElement = document.getElementById('contentwebflow');
      contentElement.scrollIntoView({ behavior: 'smooth' });}