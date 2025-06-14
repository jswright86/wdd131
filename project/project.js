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

// Project data for each skill level
const projectsData = {
    beginner: [
        {
            image: "bracelet.webp",
            caption: "Elegant Hole Saw Bracelet",
            url: "https://www.woodmagazine.com/project-plans/free/free-elegant-hole-saw-bracelet-woodworking-plan",
            loading: "lazy"
        },
        {
            image: "clock.webp",
            caption: "Art Deco Desk Clock",
            url: "https://www.woodmagazine.com/project-plans/free/free-art-deco-desk-clock-woodworking-plan",
            loading: "lazy"
        },
        {
            image: "shelves.webp",
            caption: "Floating Wall Shelves",
            url: "https://www.woodmagazine.com/project-plans/furniture/bookcases-shelving/floating-wall-shelves-downloadable-plan",
            loading: "lazy"
        },
        {
            image: "picture_frame.webp",
            caption: "Picture Frame",
            url: "https://www.woodmagazine.com/woodworking-plans/gifts-accessories/picture-frame-woodworking-plan",
            loading: "lazy"
        },
        {
            image: "tablesaw_workbench.webp",
            caption: "Space-saving Double-duty Tablesaw Workbench",
            url: "https://www.woodmagazine.com/project-plans/free/free-plan-space-saving-double-duty-tablesaw-workbench",
            loading: "lazy"
        },
        {
            image: "flagcase.webp",
            caption: "Flag Case",
            url: "https://www.woodmagazine.com/project-plans/free/flag-case",
            loading: "lazy"
        },
        {
            image: "play_center.webp",
            caption: "Keep It Tidy Play Center",
            url: "https://www.woodmagazine.com/woodworking-plans/gifts-accessories/wood-toys/keep-it-tidy-play-center-plan",
            loading: "lazy"
        },
        {
            image: "easel.webp",
            caption: "Young Artist's Easel",
            url: "https://www.woodmagazine.com/woodworking-plans/gifts-accessories/wood-toys/young-artists-easel-woodworking-plan",
            loading: "lazy"
        }
    ],
    experienced: [
        {
            image: "roll_island.webp",
            caption: "Rolling Kitchen Island",
            url: "https://www.woodmagazine.com/project-plans/furniture/cabinets-storage/rolling-kitchen-island-downloadable-plan",
            loading: "lazy"
        },
        {
            image: "classic_bookcase.webp",
            caption: "Classic Bookcase",
            url: "https://www.woodmagazine.com/project-plans/furniture/bookcases-shelving/classic-bookcase-downloadable-plan",
            loading: "lazy"
        },
        {
            image: "study_desk.webp",
            caption: "Built-to-Suit Study Desk",
            url: "https://www.woodmagazine.com/project-plans/furniture/desks/build-to-suit-study-desk-downloadable-plan",
            loading: "lazy"
        },
        {
            image: "farmhouse_table.webp",
            caption: "Farmhouse Table and Benches",
            url: "https://www.woodmagazine.com/project-plans/furniture/tables/farmhouse-table-woodworking-plan",
            loading: "lazy"
        },
        {
            image: "garden_bench.webp",
            caption: "Outdoor Garden Bench",
            url: "https://www.familyhandyman.com/garden-bench",
            loading: "lazy"
        },
        {
            image: "potting_bench.webp",
            caption: "Potting Bench",
            url: "https://www.woodmagazine.com/woodworking-plans/free/potting-bench",
            loading: "lazy"
        },
        {
            image: "mobile_crane.webp",
            caption: "Construction-grade Mobile Crane",
            url: "https://www.woodmagazine.com/woodworking-plans/free/mobile-crane",
            loading: "lazy"
        },
        {
            image: "display_case.webp",
            caption: "Bow-front Display Case",
            url: "https://www.woodmagazine.com/woodworking-plans/furniture/living-room/free-bow-front-display-case-plan",
            loading: "lazy"
        }
        
    ],
    master: [
        {
            image: "media_center.webp",
            caption: "Component-Ready Flat-Screen Media Center",
            url: "https://www.woodmagazine.com/project-plans/furniture/entertainment-centers/component-ready-flat-screen-media-center-downloadable",
            loading: "lazy"
        },
        {
            image: "entertain_center.webp",
            caption: "Home Entertainment Center",
            url: "https://www.woodmagazine.com/woodworking-plans/furniture/living-room/compact-home-entertainment-center-plan",
            loading: "lazy"
        },
        {
            image: "nesting_end_table.webp",
            caption: "Nesting End Tables",
            url: "https://www.woodmagazine.com/woodworking-plans/free/nesting-end-tables-plan",
            loading: "lazy"
        },
        {
            image: "pencil_bed.webp",
            caption: "Pencil Post Bed",
            url: "https://www.woodmagazine.com/project-plans/furniture/bed-bedroom-sets/pencil-post-bed-downloadable-plan",
            loading: "lazy"
        },
        {
            image: "keepsake_box.webp",
            caption: "Keepsake Box",
            url: "https://www.woodmagazine.com/project-plans/free/free-plan-keepsake-box",
            loading: "lazy"
        },
        {
            image: "shaker_dresser.webp",
            caption: "Shaker- Style Dresser with Mirror",
            url: "https://www.woodmagazine.com/project-plans/furniture/bed-bedroom-sets/shaker-style-dresser-with-valet-and-mirror-downloadable",
            loading: "lazy"
        },
        {
            image: "builtin_bookcase.webp",
            caption: "Built-In Bookcase",
            url: "https://www.woodmagazine.com/woodworking-plans/free/free-built-in-bookcase-and-cabinet-plan",
            loading: "lazy"
        },
        {
            image: "end_table.webp",
            caption: "Supercharged End Table",
            url: "https://www.woodmagazine.com/project-plans/free/free-plan-supercharged-end-table",
            loading: "lazy"
        },
        
    ]
};

let currentGroupIndex = 0;
const imagesPerGroup = 4;
const totalGroups = Math.ceil(imageArray.length / imagesPerGroup);

// Create carousel structure
function createCarousel() {
    const container = document.querySelector('.image-container');
    const indicatorContainer = document.querySelector('.page-indicator');
   

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

    // Buttons are always enabled for looping carousel
    prevBtn.disabled = false;
    nextBtn.disabled = false;

    // Update indicator dots
    indicators.forEach((dot, index) => {
        dot.classList.toggle('active', index === currentGroupIndex);
    });
}

// Navigation functions with looping
function goToNextGroup() {
    // Loop back to first group after last group
    currentGroupIndex = (currentGroupIndex + 1) % totalGroups;
    showCurrentGroup();
}

function goToPrevGroup() {
    // Loop to last group when going backwards from first group
    currentGroupIndex = currentGroupIndex === 0 ? totalGroups - 1 : currentGroupIndex - 1;
    showCurrentGroup();
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

// Function to display home content
function showHomeContent() {
    const projectsContainer = document.querySelector('.projects-click')
    
    // Clear existing content
    projectsContainer.innerHTML = '';
    
    // Create the home content section
    const homeSection = document.createElement('section');
    homeSection.className = 'intro';
    
    // Create title
    const title = document.createElement('h2');
    title.textContent = 'The Woodworkers Guide';
    
    // Create first paragraph
    const paragraph1 = document.createElement('p');
    paragraph1.textContent = "The ultimate guide for those who are into woodworking. Tips, tricks, how to's and project's for individuals ranging from beginner to master.";
    
    // Create second paragraph with styled span
    const paragraph2 = document.createElement('p');
    paragraph2.innerHTML = 'Our <span>Purpose</span> is to provide a comprehensive guide for woodworking enthusiasts of all skill levels. Whether you\'re a beginner looking for your first project or a seasoned pro seeking advanced techniques, we\'ve got you covered.';
    
    // Append elements to section
    homeSection.appendChild(title);
    homeSection.appendChild(paragraph1);
    homeSection.appendChild(paragraph2);
    
    // Create the profile image
    const profileImg = document.createElement('img');
    profileImg.src = 'profile_photo.webp';
    profileImg.alt = 'Woodworker Image';
    profileImg.width = 500;
    profileImg.id = 'profile';
    profileImg.loading = 'lazy';
    
    // Append both elements to the projects container
    projectsContainer.appendChild(homeSection);
    projectsContainer.appendChild(profileImg);
    
    
}

// Function to display projects for a specific skill level
function showProjects(skillLevel) {
    const projectsContainer = document.querySelector('.projects-click');
    const projects = projectsData[skillLevel];
    
    
    
    // Clear existing content
    projectsContainer.innerHTML = '';
    
    // Create title for the skill level
    const title = document.createElement('h2');
    title.className = 'project-title';
    title.textContent = `${skillLevel.charAt(0).toUpperCase() + skillLevel.slice(1)} Projects`;
    projectsContainer.appendChild(title);
    
    // Create projects grid container
    const projectsGrid = document.createElement('div');
    projectsGrid.className = 'projects-grid';
    
    // Add each project to the grid
    projects.forEach(project => {
        const projectCard = document.createElement('div');
        projectCard.className = 'project-card';
        
        // Create clickable link
        const projectLink = document.createElement('a');
        projectLink.href = project.url;
        projectLink.target = '_blank';
        projectLink.rel = 'noopener noreferrer';
        
        // Create image
        const img = document.createElement('img');
        img.src = project.image;
        img.alt = project.caption;
        img.loading = 'lazy';
        
        // Create caption
        const caption = document.createElement('div');
        caption.className = 'project-caption';
        caption.textContent = project.caption;
        
        // Assemble the project card
        projectLink.appendChild(img);
        projectLink.appendChild(caption);
        projectCard.appendChild(projectLink);
        projectsGrid.appendChild(projectCard);
    });
    
    projectsContainer.appendChild(projectsGrid);
    
    // Scroll to projects section
    projectsContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Dropdown functionality
function createDropdownMenu() {
    // Find the Projects link in the navigation
    const nav = document.querySelector('nav ul');
    const projectsLink = nav.querySelector('a[href="projects.html"]');
    
    
    
    
    // Get the parent li element
    const projectsLi = projectsLink.parentElement;
    
    // Add dropdown class and make it a container
    projectsLi.classList.add('dropdown');
    
    // Create dropdown menu
    const dropdownMenu = document.createElement('ul');
    dropdownMenu.classList.add('dropdown-menu');
    
    // Create dropdown items with click handlers
    const dropdownItems = [
        { text: 'Beginner', href: '#beginner', skillLevel: 'beginner' },
        { text: 'Experienced', href: '#experienced', skillLevel: 'experienced' },
        { text: 'Master', href: '#master', skillLevel: 'master' }
    ];
    
    dropdownItems.forEach(item => {
        const li = document.createElement('li');
        const a = document.createElement('a');
        a.href = item.href;
        a.textContent = item.text;
        
        // Add click event to show projects
        a.addEventListener('click', (e) => {
            e.preventDefault();
            showProjects(item.skillLevel);
            dropdownMenu.classList.remove('show');
        });
        
        li.appendChild(a);
        dropdownMenu.appendChild(li);
    });
    
    // Add dropdown menu to the Projects li
    projectsLi.appendChild(dropdownMenu);
    
    // Add event listeners for dropdown functionality
    let dropdownTimeout;
    
    // Show dropdown on hover
    projectsLi.addEventListener('mouseenter', () => {
        clearTimeout(dropdownTimeout);
        dropdownMenu.classList.add('show');
    });
    
    // Hide dropdown when mouse leaves
    projectsLi.addEventListener('mouseleave', () => {
        dropdownTimeout = setTimeout(() => {
            dropdownMenu.classList.remove('show');
        }, 150); // Small delay to prevent flickering
    });
    
    // Handle click on main Projects link
    projectsLink.addEventListener('click', (e) => {
        e.preventDefault();
        // Toggle dropdown on click for mobile/touch devices
        dropdownMenu.classList.toggle('show');
    });
    
    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
        if (!projectsLi.contains(e.target)) {
            dropdownMenu.classList.remove('show');
        }
    });
}

// Function to setup home link functionality
function setupHomeLink() {
    const homeLink = document.querySelector('nav a[href="home.html"]');
    
    if (homeLink) {
        homeLink.addEventListener('click', (e) => {
            e.preventDefault();
            showHomeContent();
        });
    }
}

// Initialize everything when DOM is loaded
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
    
    // Initialize dropdown menu
    createDropdownMenu();
    
    // Setup home link functionality
    setupHomeLink();
    
    // Show home content by default
    showHomeContent();
    
    console.log(`Carousel initialized with ${totalGroups} groups of images`);
    console.log('Dropdown menu initialized');
    console.log('Projects system ready');
    console.log('Home content functionality added');
});
