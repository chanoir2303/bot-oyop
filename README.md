# bot-oyop

## How to set up the bot in discord
### Create an app
Create a new application from [discord developer portal](https://discord.com/developers/applications)

<img width="816" alt="Capture d’écran 2023-01-22 à 19 34 32" src="https://user-images.githubusercontent.com/80722034/213936357-14694c20-d7af-4c54-951c-f5c49eaf747a.png">

### Create a bot
Select the app newly created and add a bot

<img width="329" alt="Capture d’écran 2023-01-22 à 19 36 58" src="https://user-images.githubusercontent.com/80722034/213936454-369f2480-9c34-4efb-9339-cf0816b0136d.png">

### Add permissions
Configure bot whether differents permissions than **oyop** needed (**oyop** use Administrator permission)

<img width="927" alt="Capture d’écran 2023-01-22 à 19 40 34" src="https://user-images.githubusercontent.com/80722034/213936690-338fa92f-10e6-41f9-a632-55fcd48a90cb.png">


### Generate TOKEN
Generate TOKEN from OAuth2 section, add it to the config file of the project

<img width="257" alt="Capture d’écran 2023-01-22 à 19 41 27" src="https://user-images.githubusercontent.com/80722034/213936640-fe8dbcdd-e23c-47bc-8aad-27d42e4e2d7a.png">

## More...
Make sure in your code that the discord app config looks like the sample below if you use **oyop**

`default_intents = discord.Intents.all()`
