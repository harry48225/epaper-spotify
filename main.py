from waveshare_epd import epd2in13_V2

from ImageCreator import ImageCreator

epd = epd2in13_V2.EPD()

epd.init(epd.FULL_UPDATE)
epd.Clear(0xFF)

i = ImageCreator()

epd.display(epd.getbuffer(i.get_image()))
    