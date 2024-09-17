
document.addEventListener('DOMContentLoaded', () => {
    const video = document.getElementById('video');
    const emotionIcon = document.getElementById('emotion-icon');
    const emotionDescription = document.getElementById('emotion-description');
    const audioPlayer = document.getElementById('audio-player');
    const lottieContainer = document.getElementById('lottie-animation');

    async function startCamera() {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            video.srcObject = stream;
        } catch (err) {
            console.error('Error accessing webcam: ', err);
        }
    }

    function detectEmotion() {
        // Placeholder for actual emotion detection logic
        setTimeout(() => {
            const detectedEmotion = getMockEmotion();
            updateEmotionDisplay(detectedEmotion);
            updateMusicRecommendation(detectedEmotion);
        }, 2000);
    }

    function getMockEmotion() {
        const emotions = [
            { icon: '😊 happy', description: 'Happy', music: '1.mp3' },
            { icon: '😢', description: 'Sad', music: '2.mp3' },
            { icon: '😡', description: 'Angry', music: '3.mp3' },
            { icon: '😮', description: 'Surprised', music: '4.mp3'},
            { icon: '😨', description: 'Fear', music: '4.mp3'},
            { icon: '😑', description: 'Disgust', music: '4.mp3'},
        ];
        return emotions[Math.floor(Math.random() * emotions.length)];
    }

    function updateEmotionDisplay(emotion) {
        emotionIcon.textContent = emotion.icon;
        emotionDescription.textContent = emotion.description;
    }

    function updateMusicRecommendation(emotion) {
        audioPlayer.src = music/$;{emotion.music}; // Updated path to the 'music' folder
        audioPlayer.load();
        audioPlayer.play();
    }

    function initLottieAnimation() {
        const animation = lottie.loadAnimation({
            container: lottieContainer,
            renderer: 'svg',
            loop: true,
            autoplay: true,
            path: 'path/to/lottie/animation.json' // Replace with your Lottie animation file path
        });
    }

    document.querySelectorAll('nav a').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    document.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            document.querySelector('header').classList.add('scrolled');
        } else {
            document.querySelector('header').classList.remove('scrolled');
        }
    });

    startCamera();
    initLottieAnimation();
    setInterval(detectEmotion, 5000);
});

document.addEventListener('DOMContentLoaded', () => {
    const video = document.getElementById('video');
    const emotionIcon = document.getElementById('emotion-icon');
    const emotionDescription = document.getElementById('emotion-description');
    const audioPlayer = document.getElementById('audio-player');
    const audioSource = document.getElementById('audio-source');
    const musicDropdown = document.getElementById('music-dropdown');
    const lottieContainer = document.getElementById('lottie-animation');

    async function startCamera() {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            video.srcObject = stream;
        } catch (err) {
            console.error('Error accessing webcam: ', err);
        }
    }

    function detectEmotion() {
        // Placeholder for actual emotion detection logic
        setTimeout(() => {
            const detectedEmotion = getMockEmotion();
            updateEmotionDisplay(detectedEmotion);
            updateMusicRecommendation(detectedEmotion);
        }, 2000);
    }

    function getMockEmotion() {
        const emotions = [
            { icon: '😊', description: 'Happy', music: '1.mp3' },
            { icon: '😢', description: 'Sad', music: '2.mp3' },
            { icon: '😡', description: 'Angry', music: '3.mp3' },
        ];
        return emotions[Math.floor(Math.random() * emotions.length)];
    }

    function updateEmotionDisplay(emotion) {
        emotionIcon.textContent = emotion.icon;
        emotionDescription.textContent = emotion.description;
    }

    function updateMusicRecommendation(emotion) {
        audioSource.src = music/$;{emotion.music};
        audioPlayer.load();
        audioPlayer.play();
    }

    // Event listener for dropdown change
    musicDropdown.addEventListener('change', (event) => {
        const selectedTrack = event.target.value;
        audioSource.src = music/$;{selectedTrack};
        audioPlayer.load();
        audioPlayer.play();
    });

    function initLottieAnimation() {
        const animation = lottie.loadAnimation({
            container: lottieContainer,
            renderer: 'svg',
            loop: true,
            autoplay: true,
            path: 'path/to/lottie/animation.json' // Replace with your Lottie animation file path
        });
    }

    document.querySelectorAll('nav a').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    document.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            document.querySelector('header').classList.add('scrolled');
        } else {
            document.querySelector('header').classList.remove('scrolled');
        }
    });

    startCamera();
    initLottieAnimation();
    setInterval(detectEmotion, 5000);
});

/* MUSIC FILE CODES */


// Function to toggle the dropdown
function toggleDropdown() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      for (var i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }
  