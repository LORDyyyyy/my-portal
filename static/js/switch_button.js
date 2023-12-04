document.addEventListener('DOMContentLoaded', function ()
{
	const darkModeToggle = document.getElementById('toggle-dark-mode');
	const body = document.body;
	const isDarkMode = localStorage.getItem('darkMode') === 'enabled';

	if (isDarkMode)
	{
		body.classList.add('dark-mode');
		document.getElementById('toggle-dark-mode').checked = true;;
	}

	darkModeToggle.addEventListener('click', function ()
	{
		body.classList.toggle('dark-mode');

		if (body.classList.contains('dark-mode'))
		{
			localStorage.setItem('darkMode', 'enabled');
		} else
		{
			localStorage.setItem('darkMode', 'disabled');
		}
	});
});

