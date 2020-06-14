# owobot-python

An anime pics bot ~~for Telegram~~ as universal module, written on ~~java~~python, which takes data from reddit and returns URL of picture.
Бот ~~для телеграмма~~ написанный как универ-ый модуль, присылающий аниме девочек, написанный на ~~java~~python, берущий данные из reddit и возвращающий URL картинки.

Original bot link ([by ASPIRINswag](https://github.com/ASPIRINswag/owobot-java)) :  [@owopics_bot](https://t.me/owopics_bot)

### Features
* ~~Multi~~Singlethreading
* Works great in group chats
* Preverting timeout errors
* ~~Chat related NSFW settings~~ Always(almost) NSFW
* ~~User related language settings (english and russian)~~ Feedbacks with URL or `False`
* Cannot answer on `owo` and `uwu`
* Returns only `.jpg` or `.png`, but you can edit the code for needed types by yourself

### How to use
1. Go to [@owopics_bot](https://t.me/owopics_bot) and just use the bot!
2. Or use as module in your project.

Or if for some reason you want to run it by yourself:

0. Install `praw` with `pip` or somehow else.
1. Clone code to somewhere
2. `import owobot`
3. `owobot.Session(client_id, client_secret, user_agent)` takes three required arguments for read-only session.
4. `owobot.GetPicSFW` - Returns URL of picture from SFW subreddits.
4.1 `owobot.GetPicNSFW` - E-eh, i think you know it better.

### Reason of choosing some questionable solutions
1. ~~I'm java newbie~~, although it's he, not me
2. it was written with keeping in mind idea about implementation all features just with python, without anything outside like java crap or something like that, even without any proxy settings, cuz it's a module lol.

### TODO
- [ ] Rewrite in YoptaScript someday
