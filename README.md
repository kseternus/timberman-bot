![ezgif com-video-to-gif-converter(3)](https://github.com/user-attachments/assets/a86e3316-94c6-4c23-b7ce-1f3f4d67991b)<br />
<br />
The script used ImageGrab (PIL is now only used for screenshot comparisons), but unfortunately the speed of cutting trees<br />
was too slow due to the delay during screenshot taking. ImageGrab was replaced with mss which significantly sped up<br />
the program. The program works by initially taking two screenshots on the left and right side of the tree above the player<br />
for further comparison.<br />
<br />
![20241023161907_1](https://github.com/user-attachments/assets/8bad5268-d387-4b6c-92a8-5c28f32fd811)<br />
<br />
After running the script, the user starts the game, pressing the 's' button, the script starts, the above-mentioned screenshots<br />
are taken. The program constantly presses the left arrow cutting trees while taking a screenshot of the left area comparing<br />
it with the base area. If it detects a change (branch), it changes the flag for cutting trees on the left to False and moves<br />
to the right, continuing the principle of operation on the right side. By pressing the 'q' button we stop the script.<br />
We can run it again by pressing 's', thus taking new base screenshots.<br />
<br />
Update:<br />
Changed some speed of cutting and area of screenshots<br />
Highest score i managed to get was 11516<br />
