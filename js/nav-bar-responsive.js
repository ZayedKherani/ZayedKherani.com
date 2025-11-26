function toggleMenu() {
  const navbarDiv = document.querySelector("nav.nav-bar ul div#nav-bar.right");
  const menuIconPath = document.querySelector(
    "li.responsive-navbar-menu a svg path"
  );

  const navBarHeight = document.querySelector("nav.nav-bar").offsetHeight;

  if (navbarDiv.className === "right") {
    navbarDiv.className = "right responsive";

    menuIconPath.setAttribute("d", "M64 160C64 142.3 78.3 128 96 128L480 128C497.7 128 512 142.3 512 160C512 177.7 497.7 192 480 192L96 192C78.3 192 64 177.7 64 160zM128 320C128 302.3 142.3 288 160 288L544 288C561.7 288 576 302.3 576 320C576 337.7 561.7 352 544 352L160 352C142.3 352 128 337.7 128 320zM512 480C512 497.7 497.7 512 480 512L96 512C78.3 512 64 497.7 64 480C64 462.3 78.3 448 96 448L480 448C497.7 448 512 462.3 512 480z");

    const responsiveNavBarDiv = document.querySelector(
      "nav.nav-bar ul div#nav-bar.right.responsive"
    );

    if (responsiveNavBarDiv) {
      responsiveNavBarDiv.style.top = `${navBarHeight}px`;
    }
  } else {
    navbarDiv.className = "right";

    menuIconPath.setAttribute("d", "M96 160C96 142.3 110.3 128 128 128L512 128C529.7 128 544 142.3 544 160C544 177.7 529.7 192 512 192L128 192C110.3 192 96 177.7 96 160zM96 320C96 302.3 110.3 288 128 288L512 288C529.7 288 544 302.3 544 320C544 337.7 529.7 352 512 352L128 352C110.3 352 96 337.7 96 320zM544 480C544 497.7 529.7 512 512 512L128 512C110.3 512 96 497.7 96 480C96 462.3 110.3 448 128 448L512 448C529.7 448 544 462.3 544 480z");
  }
}
