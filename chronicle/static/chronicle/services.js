
	  let currentIndex = 0;
	
	  function showSlide(index) {
		const slider = document.querySelector('.slider');
		const slideWidth = document.querySelector('.slide').offsetWidth;
		const newPosition = -index * slideWidth;
		slider.style.transform = `translateX(${newPosition}px)`;
	  }
	
	  function prevSlide() {
		currentIndex = (currentIndex - 1 + 9) % 9; // Adjust the number based on the total number of slides
		showSlide(currentIndex);
	  }
	
	  function nextSlide() {
		currentIndex = (currentIndex + 1) % 9; // Adjust the number based on the total number of slides
		showSlide(currentIndex);
	  }
	
	  // Auto-slide every 1 second
	  setInterval(() => {
		nextSlide();
	  }, 3000);

     // JavaScript function to scroll down when the link is clicked
      function scrollToContentpython() {
        const contentElement = document.getElementById('contentpython');
        contentElement.scrollIntoView({ behavior: 'smooth' });
        }
		// JavaScript function to scroll down when the link is clicked
	  function scrollToContentdjango() {
        const contentElement = document.getElementById('contentdjango');
        contentElement.scrollIntoView({ behavior: 'smooth' });
        }
		// JavaScript function to scroll down when the link is clicked
	  function scrollToContenthtml() {
        const contentElement = document.getElementById('contenthtml');
        contentElement.scrollIntoView({ behavior: 'smooth' });
        }
		// JavaScript function to scroll down when the link is clicked
	  function scrollToContentbs() {
        const contentElement = document.getElementById('contentbs');
        contentElement.scrollIntoView({ behavior: 'smooth' });
        }
		// JavaScript function to scroll down when the link is clicked
	  function scrollToContentselenium() {
        const contentElement = document.getElementById('contentselenium');
        contentElement.scrollIntoView({ behavior: 'smooth' });
        }
		// JavaScript function to scroll down when the link is clicked
	  function scrollToContentscrapy() {
        const contentElement = document.getElementById('contentscrapy');
        contentElement.scrollIntoView({ behavior: 'smooth' });
        }
		// JavaScript function to scroll down when the link is clicked
	  function scrollToContentwordpress() {
        const contentElement = document.getElementById('contentwordpress');
        contentElement.scrollIntoView({ behavior: 'smooth' });
        }
		// JavaScript function to scroll down when the link is clicked
	  function scrollToContentwebflow() {
        const contentElement = document.getElementById('contentwebflow');
        contentElement.scrollIntoView({ behavior: 'smooth' });
        }
		// JavaScript function to scroll down when the link is clicked
	  function scrollToContentexcel() {
        const contentElement = document.getElementById('contentexcel');
        contentElement.scrollIntoView({ behavior: 'smooth' });
        }
