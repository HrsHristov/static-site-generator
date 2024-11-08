block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    nodes = []
    for block in blocks:
        stripped_block = block.strip()
        if len(stripped_block) == 0:
            continue
        nodes.append(stripped_block)
    return nodes

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph

    # quotes_counter = 0
    # ul_counter = 0
    # ol_counter = 0

    # for l in range(len(lines)):
    #     if lines[l].startswith(">"):
    #         quotes_counter += 1
    #     if lines[l].startswith("* ") or lines[l].startswith("- "):
    #         ul_counter += 1
    #     if lines[l].startswith(f"{l + 1}. "):
    #         ol_counter +=1

    # if quotes_counter == len(lines):
    #     return "quote"
    
    # if ul_counter == len(lines):
    #     return "unordered_list"
    
    # if ol_counter == len(lines):
    #     return "ordered_list"
    
    # return "paragraph"