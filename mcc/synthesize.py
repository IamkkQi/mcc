# -*- coding: utf-8 -*-
import os
import fnmatch
import click
from pydub import AudioSegment


@click.command()
@click.option('--sound', '-s', multiple=True, help='需要合成的话术')
@click.option('--filesdir', '-d', help='变量语音所在文件夹')
@click.option('--tdir', '-td', help='合成后语音存放的路径')
def main(sound, filesdir, tdir):
    """ 批量话术拼接变量语音 """

    # print(f'{sound}---{filesdir}---{tdir}')
    # 创建合成后语音文件夹
    if not os.path.exists(tdir):
        os.makedirs(tdir)

    # 获取第一段话术语音
    # for s in sound:
    if len(sound) == 1:
        sound_1 = AudioSegment.from_wav(sound[0])
        sound_2 = AudioSegment.empty()
    else:
        sound_1 = AudioSegment.from_wav(sound[0])
        sound_2 = AudioSegment.from_wav(sound[1])

    for file in os.listdir(filesdir):
        if fnmatch.fnmatch(file, '*.wav'):
            sound_f = AudioSegment.from_wav(f'{filesdir}/{file}')
            file_n = f'{file.split(".")[0]}_话术'  # 合成语音的文件名
            result = sound_1 + sound_f + sound_2  # 合成后的语音文件
            result.export(f'{tdir}/{file_n}.wav', format='wav')
