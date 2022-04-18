import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
    def init(self, client):
        self.client = client

    @commands.command(aliases=['lisa'])  #리사 보이스 채널 입장: "리사","lisa"
    async def 리사(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("당신은 보이스 채널에 들어와 있지 않습니다.")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command(aliases=["나가", "out", "리사 나가"])   #리사 보이스채널 퇴장: "나가","out","리사 나가","리사나가"
    async def 리사나가(self, ctx):
       await ctx.voice_client.disconnect()

    @commands.command(aliases=["노래 재생", "재생", "노래"])    #노래재생/url포함 "노래재생", "노래 재생", "재생", "노래"
    async def 노래재생(self,ctx,url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download = False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command(aliases=["멈춰", "노래 멈춰", "노래 중지", "노래중지"])     #재생중이던 노래 중지: "중지","멈춰","노래 멈춰", "노래 중지", "노래중지"
    async def 중지(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("중지")

    @commands.command()     #중지한 노래 다시재생: "다시재생"
    async def 다시재생(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("재생")


def setup(client):
    client.add_cog(music(client))