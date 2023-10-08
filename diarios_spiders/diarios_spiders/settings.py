
BOT_NAME = 'diarios_spiders'

SPIDER_MODULES = ['diarios_spiders.spiders']
NEWSPIDER_MODULE = 'diarios_spiders.spiders'

ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {'diarios_spiders.pipelines.DiariosSpidersPipeline': 1}
FILES_STORE = 'diarios'
