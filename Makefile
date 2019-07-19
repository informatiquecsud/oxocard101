livehtml:
	watchmedo shell-command --patterns="*.rst;*.py" --recursive  --command='runestone build && runestone serve'
