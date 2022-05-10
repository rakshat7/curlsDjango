let darkMode = localStorage.getItem("darkMode");
const darkModeToggle = document.getElementById("theme-btn");

const enableDarkMode = () => {
    document.body.classList.add("dark-mode");
    darkModeToggle.src = "../static/img/beardW.png";
    localStorage.setItem("darkMode","enabled");
};

const disableDarkMode = () => {
    document.body.classList.remove("dark-mode");
    darkModeToggle.src = "../static/img/beard.png";
    localStorage.setItem("darkMode",null);
};

if(darkMode === "enabled")
{
    enableDarkMode();
}

darkModeToggle.addEventListener("click",() => {
    darkMode = localStorage.getItem("darkMode");
    if(darkMode !== "enabled")
    {
        enableDarkMode();
    }
    else{
        disableDarkMode();
    }
});


// Datatable Initialization 

// $(document).ready(function(){
//     var dataTable = $("#serviceTable").DataTable();

// });

