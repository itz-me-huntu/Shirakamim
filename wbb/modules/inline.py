# flake8: noqa F405
"""
MIT License

Copyright (c) 2021 TheHamkerCat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import traceback

from wbb import app
from wbb.utils.inlinefuncs import *

__MODULE__ = "Inline"
__HELP__ = """
Inline commands can be used by anyone via inline.

Syntax:
   @OdaRobot [command] [query]

Commands Available:
- alive - Check Bot's Stats.
- yt [query] - Youtube Search.
- tr [LANGUAGE_CODE] [QUERY]** - Translate Text.
- lyrics [QUERY] - Search Song Lyrics
- google [QUERY] - Google Search.
- info [ID/USERNAME] - Get Profile User Telegram.
-chat_info [ID/USERNAME GROUP] - Get Profile Group Telegram.
- bitly [URL] - Shorten A Link.
- wall [Query] - Find Wallpapers.
- image [Query] - Find pictures.
- ytmusic [SONG_NAME] - Get Songs From Youtube Music.
- music [SONG_NAME] - Get Songs.
- torrent [QUERY] - Torrent Search.
- tmdb [QUERY] - Search movies on imdb.
- gh_repo [QUERY] - Search github repo.
- gh_user [QUERY] - Search github user.
- wiki [QUERY] - Search wikipedia.
- ping - Check ping rate.
- ud [QUERY] - Urban Dictionary Query.
-speedtest - Check Speed Server.
-pypi [PACKAGE NAME] - Check pkg/pip Python."""


@app.on_inline_query()
async def inline_query_handler(client, query):
    try:
        text = query.query.strip().lower()
        answers = []
        if text.strip() == "":
            answerss = await inline_help_func(__HELP__)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=10
            )
            return
        elif text.split()[0] == "alive":
            answerss = await alive_function(answers)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=10
            )
        elif text.split()[0] == "tr":
            if len(text.split()) < 3:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Translator | tr [LANG] [TEXT]",
                    switch_pm_parameter="inline",
                )
            lang = text.split()[1]
            tex = text.split(None, 2)[2].strip()
            answerss = await translate_func(answers, lang, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss,
            )
        elif text.split()[0] == "ud":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Urban Dictionary | ud [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await urban_func(answers, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss,
            )
        elif text.split()[0] == "google":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Google Search | google [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await google_search_func(answers, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss,
            )
        elif text.split()[0] == "bitly":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Link Shortener | bitly [LINK]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await shortify(tex)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )

        elif text.split()[0] == "wall":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    is_gallery=True,
                    switch_pm_text="Wallpapers Search | wall [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await wall_func(answers, tex)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )

        elif text.split()[0] == "torrent":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Torrent Search | torrent [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await torrent_func(answers, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss,
            )

        elif text.split()[0] == "yt":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="YouTube Search | yt [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await youtube_func(answers, tex)
            await client.answer_inline_query(
                query.id, results=answerss
            )

        elif text.split()[0] == "lyrics":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Lyrics Search | lyrics [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await lyrics_func(answers, tex)
            await client.answer_inline_query(
                query.id, results=answerss
            )

        elif text.split()[0] == "gh_user":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Github User | gh_user [USERNAME/LINK]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await github_user_func(answers, tex)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )

        elif text.split()[0] == "gh_repo":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Github Repo Search | [LINK]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await github_repo_func(answers, tex)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )

        elif text.split()[0] == "search":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Global Message Search. | search [QUERY]",
                    switch_pm_parameter="inline",
                )
            user_id = query.from_user.id
            tex = text.split(None, 1)[1].strip()
            answerss = await tg_search_func(answers, tex, user_id)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )

        elif text.split()[0] == "music":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Music Search | music [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await music_inline_func(answers, tex)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )

        elif text.split()[0] == "wiki":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Wikipedia | wiki [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await wiki_func(answers, tex)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )

        elif text.split()[0] == "speedtest":
            answerss = await speedtest_init(query)
            return await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )

        elif text.split()[0] == "pmpermit":
            user_id = query.from_user.id
            victim = text.split()[1]
            answerss = await pmpermit_func(answers, user_id, victim)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )

        elif text.split()[0] == "ping":
            answerss = await ping_func(answers)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )

        elif text.split()[0] == "ytmusic":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="YT Music | ytmusic [url]",
                    switch_pm_parameter="inline",
                )
            tex = query.query.split(None, 1)[1].strip()
            answerss = await yt_music_func(answers, tex)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )

        elif text.split()[0] == "info":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="User Info | info [USERNAME|ID]",
                    switch_pm_parameter="inline",
                )
            tex = text.split()[1].strip()
            answerss = await user_info_inline_func(answers, tex)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )

        elif text.split()[0] == "chat_info":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Chat Info | chat_info [USERNAME|ID]",
                    switch_pm_parameter="inline",
                )
            tex = text.split()[1].strip()
            answerss = await chat_info_inline_func(answers, tex)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )

        elif text.split()[0] == "tmdb":
            if len(text.split()) < 2:
                answerss = await tmdb_func(answers, "")
                return await client.answer_inline_query(
                    query.id,
                    results=answerss,
                    switch_pm_text="TMDB Search | tmdb [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split()[1].strip()
            answerss = await tmdb_func(answers, tex)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )

        elif text.split()[0] == "pypi":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Pypi Search | pypi [Package Name]",
                    switch_pm_parameter="inline",
                )
            tex = text.split()[1].strip()
            answerss = await pypiSearchFunc(answers, tex)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )

        elif text.split()[0] == "image":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    is_gallery=True,
                    switch_pm_text="Image Search | image [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await image_func(answers, tex)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=3600
            )

    except Exception as e:
        e = traceback.format_exc()
        print(e, " InLine")
