# -*- coding: utf-8 -*-

"""Console script for mcc."""
import os
import click
# from pydub import AudioSegment
# from pydub.silence import split_on_silence


@click.command()
@click.argument('sound_path')
@click.option('--mls', default=500, help='沉默的时长，毫秒')
@click.option('--st', default=-30, help='无声的界限，如果比这个数值更小则认为是无声')
@click.option('--name', default=0, help='分割出来文件的名字，默认从0开始')
def main(sound_path, mls, st, name):
    """Console script for mcc."""
    print('xixi')
    # sound = AudioSegment.from_wav(sound_path)
    # chunks = split_on_silence(sound,
    #                           # 沉默的时长, 毫秒
    #                           min_silence_len=mls,
    #                           # 如果比silence_thresh这个数值更安静则认为是无声
    #                           silence_thresh=st
    #                           )
    # print(f'碎片数量: {len(chunks)}')
    #
    # # 创建文件夹
    # dirname = f'{name}-{name + len(chunks) - 1}'
    # if not os.path.exists(dirname):
    #     os.makedirs(dirname)
    #
    # for i, chunk in enumerate(chunks):
    #     # 导出文件
    #     chunk.export(f'{dirname}/{name + i}.wav', format='wav')

