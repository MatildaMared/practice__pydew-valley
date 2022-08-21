from os import walk
import pygame


def import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):
        # filter out .DS_Store files from array
        img_files = list(filter(lambda x: x != ".DS_Store", img_files))

        for image in sorted(img_files, key=lambda x: int(x[0])):
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list
