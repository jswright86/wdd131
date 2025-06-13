 const imageArray = [
            {
                src: "tools.webp",
                alt: "Essential Tools",
                caption: "Essential Tools for Woodworking"
                
            },
            {
                src: "lumber_yard.webp",
                alt: "Lumber Yard",
                caption: "Lumber Yard Essentials"
            },
            {
                src: "diff_woods.webp",
                alt: "Different Woods",
                caption: "Different Types of Wood"
            },
            {
                src: "woodworking_proj.webp",
                alt: "Woodworking Projects",
                caption: "Woodworking Projects"
            },
            {
                src: "rubio_monocoat.webp",
                
                alt: "Wood Staining",
                caption: "Wood Staining Techniques"
            },
            {
                src: "tablesaw.webp",
                alt: "Table Saw",
                caption: "Dos and Don'ts with your most used tool"
            },
            {
                src: "workbench.webp",
                alt: "Woodworking Bench",
                caption: "Setting Up Your Workbench"
            },
            {
                src: "handtools.webp",
                alt: "Hand Tools",
                caption: "Traditional Hand Tools"
            },
            {
                src: "wood_joinery.webp",
                alt: "Wood Joints",
                caption: "Understanding Wood Joints"
            },
            {
                src: "routers.webp",
                alt: "Routers",
                caption: "All About Routers"
            },
            {
                src: "woodcarving.webp",
                alt: "Wood Carving",
                caption: "Wood Carving Artistry"
            },
            {
                src: "ppe.webp",
                alt: "Workshop Safety",
                caption: "Workshop Safety Guidelines"
            }
        ];

        let currentGroupIndex = 0;
        const imagesPerGroup = 4;
        const totalGroups = Math.ceil(imageArray.length / imagesPerGroup);

        // Create carousel structure
        function createCarousel() {
            const container = document.querySelector('.image-container');
            const indicatorContainer = document.querySelector('.page-indicator');
            
            if (!container) {
                console.error('Image container not found');
                return;
            }

            // Create indicator dots
            indicatorContainer.innerHTML = '';
            for (let i = 0; i < totalGroups; i++) {
                const dot = document.createElement('div');
                dot.className = 'indicator-dot';
                if (i === 0) dot.classList.add('active');
                dot.addEventListener('click', () => goToGroup(i));
                indicatorContainer.appendChild(dot);
            }

            // Update total groups display
            document.getElementById('total-groups').textContent = totalGroups;
            
            // Show initial group
            showCurrentGroup();
        }

        // Display current group of 4 images
        function showCurrentGroup() {
            const container = document.querySelector('.image-container');
            const startIndex = currentGroupIndex * imagesPerGroup;
            const endIndex = Math.min(startIndex + imagesPerGroup, imageArray.length);
            const currentImages = imageArray.slice(startIndex, endIndex);

            // Clear container
            container.innerHTML = '';

            // Add current group of images
            currentImages.forEach((imageData, index) => {
                const figure = document.createElement('figure');
                figure.className = 'carousel-item';
                
                const img = document.createElement('img');
                img.src = imageData.src;
                img.alt = imageData.alt;
                img.loading = 'lazy';
                
                const figcaption = document.createElement('figcaption');
                figcaption.textContent = imageData.caption;
                
                figure.appendChild(img);
                figure.appendChild(figcaption);
                container.appendChild(figure);
            });

            // Update UI indicators
            updateUI();
        }

        // Update UI elements (buttons, indicators, counter)
        function updateUI() {
            const prevBtn = document.getElementById('prev-btn');
            const nextBtn = document.getElementById('next-btn');
            const currentGroupSpan = document.getElementById('current-group');
            const indicators = document.querySelectorAll('.indicator-dot');

            // Update group counter
            currentGroupSpan.textContent = currentGroupIndex + 1;

            // Update button states
            prevBtn.disabled = currentGroupIndex === 0;
            nextBtn.disabled = currentGroupIndex === totalGroups - 1;

            // Update indicator dots
            indicators.forEach((dot, index) => {
                dot.classList.toggle('active', index === currentGroupIndex);
            });
        }

        // Navigation functions
        function goToNextGroup() {
            if (currentGroupIndex < totalGroups - 1) {
                currentGroupIndex++;
                showCurrentGroup();
            }
        }

        function goToPrevGroup() {
            if (currentGroupIndex > 0) {
                currentGroupIndex--;
                showCurrentGroup();
            }
        }

        function goToGroup(groupIndex) {
            if (groupIndex >= 0 && groupIndex < totalGroups) {
                currentGroupIndex = groupIndex;
                showCurrentGroup();
            }
        }

        // Keyboard navigation
        function handleKeyboardNavigation(event) {
            if (event.key === 'ArrowLeft') {
                goToPrevGroup();
            } else if (event.key === 'ArrowRight') {
                goToNextGroup();
            }
        }

        // Initialize carousel when page loads
        document.addEventListener('DOMContentLoaded', () => {
            // Create the carousel
            createCarousel();
            
            // Add event listeners for navigation buttons
            const nextBtn = document.getElementById('next-btn');
            const prevBtn = document.getElementById('prev-btn');
            
            if (nextBtn && prevBtn) {
                nextBtn.addEventListener('click', goToNextGroup);
                prevBtn.addEventListener('click', goToPrevGroup);
            }
            
            // Add keyboard navigation
            document.addEventListener('keydown', handleKeyboardNavigation);
            
            console.log(`Carousel initialized with ${totalGroups} groups of images`);
        });