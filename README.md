[![Issues](https://img.shields.io/github/issues/jainamoswal/ForceHub?style=for-the-badge&color=green)](https://github.com/jainamoswal/ForceHub/issues)
[![Forks](https://img.shields.io/github/forks/jainamoswal/ForceHub?style=for-the-badge&color=green)](https://github.com/jainamoswal/ForceHub/fork)
[![Stars](https://img.shields.io/github/stars/jainamoswal/ForceHub?style=for-the-badge&color=green)](https://github.com/jainamoswal/ForceHub)
[![LICENSE](https://img.shields.io/github/license/jainamoswal/ForceHub?color=green&style=for-the-badge)](https://github.com/jainamoswal/ForceHub)
[![Size](https://img.shields.io/github/repo-size/jainamoswal/ForceHub?style=for-the-badge&color=green)](https://github.com/jainamoswal/ForceHub)
[![Contributors](https://img.shields.io/github/contributors/jainamoswal/ForceHub?style=for-the-badge&color=green)](https://github.com/jainamoswal/ForceHub)

---
## Support 
- [![Channel](https://img.shields.io/badge/Telegram-Channel-green?style=for-the-badge&logo=telegram)](https://t.me/J_projects)
- [![Support](https://img.shields.io/badge/Telegram-Group-green?style=for-the-badge&logo=telegram)](https://t.me/J_projects_chat)




# ForceHub


A Telegram bot, to force a user to follow your [GitHub](https://www.github.com/jainamoswal) account before chatting.

This bot will mute the user if not followed. It works with [Telegram](https:///www.telegram.org) [Auth](https://core.telegram.org/widgets/login) and [GitHub](https:///www.github.com) [oAuth](https://docs.github.com/en/developers/apps/authorizing-oauth-apps).

---
## Steps :~ 

- Add following variables to the envirenment variables.

	- [x] `API_HASH` ~ Get it from [my.telegram.org](https://my.telegram.org/auth)

	- [x] `APP_ID` ~ Get it from [my.telegram.org](https://my.telegram.org/auth)

	- [x] `APP_DOMAIN` ~ Your application domain name. eg. https://jainam.me. 

	- [x] `BOT_TOKEN` ~ Get it from [@BotFather.](https://t.me/botfather)

	- [x] `GITHUB_USERNAME` ~ Your [GitHub](https://www.github.com/jainamoswal) username, which you want users to force-follow.

	- [x] `MONGO_URL` ~ [MongoDb](https://www.mongodb.com) URL, to save user's github usernames after login via GitHub oAuth2.

	- [x] `FLASK_SECRET_KEY` ~ Make it random value, It will be used to access session cookie while [Telegram](https://t.me/j_projects) and [GitHub](https://www.github.com/jainamoswal) linking. 

	- [x] `GITHUB_OAUTH_CLIENT_ID` ~ Your GitHub oAuth credential. Get it from [here.](https://github.com/settings/applications/new)

		> Assuming `github-app.herokuapp.com` as my App's endpoint.

		> Add App URL in GitHub app settings. eg. `https://github-app.herokuapp.com/`

		> Add App URL and a callback route to it. eg. `https://github-app.herokuapp.com/login/github/authorize`


	- [x] `GITHUB_OAUTH_CLIENT_SECRET` ~ Your GitHub oAuth credential. Get it from [here.](https://github.com/settings/applications/new)

	- [x] `PORT` ~ Leave it blank, as Heroku will assign it.


- Set the same `APP_DOMAIN` in [Bot settings.](https://core.telegram.org/widgets/login#linking-your-domain-to-the-bot)- 


---
	
### Deployments :-	

<details><summary>Heroku</summary>
<p><br>
<a href="https://dashboard.heroku.com/new?template=https://github.com/jainamoswal/ForceHub">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p>
</details>

<details><summary>Zeet</summary>
<p><br>
<a href="https://deploy.zeet.co?url=https://github.com/jainamoswal/ForceHub">
<img src="https://deploy.zeet.co/ForceHub.svg" alt="Deploy">
</a>
</p>
</details>

<details>
<summary><b>Locally</b></summary>
 <br>1. Clone it to your local machine.</br>
 <br>2. Add environment variables or remove them and use as normal varibales via setting them in <code>config.py</code></br>
 <br>3. Run both the files <code>app.py</code> & <code>ForceHub</code> via <code>python app.py</code> and <code>python -m ForceHub</code> respectively.</br>
</details>



<details>
<summary><b>Any other Platform.</b></summary>
<br>1. Clone this repo or fork it.</br>
<br>2. Set the variables as envirenment variables or in <code>config.py</code>.</br>
<br>3. Publish it.</br>
</details>


## Next pro tip :
 Use [Freenom](https://www.freenom.com) for a cool free domain.
 
 Many times, [Freenom](https://www.freenom.com) has many server issues, So you will need to retry after some time.
 

## License 
### [ForceHub](https://github.com/jainamoswal/ForceHub) is licensed under [GNU Affero General Public License v3](https://www.gnu.org/) or later.

[![License](https://www.gnu.org/graphics/gplv3-or-later.png)](LICENSE)

`The GNU General Public License (GNU GPL or simply GPL) is a series of widely-used free software licenses that guarantee end users the freedom to run, study, share, and modify the software.[8] The licenses were originally written by Richard Stallman, founder of the Free Software Foundation (FSF), for the GNU Project, and grant the recipients of a computer program the rights of the Free Software Definition.[9] The GPL series are all copyleft licenses, which means that any derivative work must be distributed under the same or equivalent license terms. This is in distinction to permissive software licenses, of which the BSD licenses and the MIT License are widely used, less restrictive examples. GPL was the first copyleft license for general use.`
