from mentions.forms import AddBlock
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Block

def blocks(request):
    block_added = False
    if request.method == 'POST':
        form = AddBlock(data=request.POST)
        if form.is_valid():
            form.save()
            block_added = True
            form = AddBlock()
    else:
        form = AddBlock()
        
    blocks_list = Block.objects.filter(moderated=True)
        
    return render_to_response('pager/blocks.html',
        {
            'block_added': mention_added,
            'blocks_list': mentions_list,
            'form': form
        },
        context_instance=RequestContext(request))
