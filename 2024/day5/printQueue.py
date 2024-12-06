def getPageRules(fileName):
    rules = []
    with open(fileName) as file: 
        for line in file:
            rules.append(tuple(map(int, line.strip().split("|"))))
            
    print(rules)
    return rules
            
def getPages(fileName):
    pages = []
    with open(fileName) as file:
        for line in file:
            pages.append(list(map(int, line.strip().split(","))))

    return pages

rules = getPageRules("pagerules.txt")
pages = getPages("pageorders.txt")

def ruleCheck(page,rules):
    for rule in rules:
        before, after = rule 
        if before in page and after in page:
            if page.index(before) > page.index(after):
                return False
    return True



def pageValidator(pages,rules):
    validPages = []
    invalidPages = []
    middlePages = []
    for page in pages:
        if ruleCheck(page,rules):
            validPages.append(page)
            middleIndex = len(page) // 2
            middlePages.append(page[middleIndex])
        else:
            invalidPages.append(page)

    print(sum(middlePages))
    return invalidPages


invalidPages = pageValidator(pages,rules)


# I really struggled with this one and had to use a lot of help from ChatGPT to understand Topological sorting and how to approach this... will need to brush up on my sorting algos A LOT.... bubble sort ;) ?
def sortPages(pages, rules):
    sortedPages = []
    middlePages = []

    for page in pages:
        pageSet = set(page)
        dependencies = {p: set() for p in page}
        for before, after in rules:
            if before in pageSet and after in pageSet:
                dependencies[after].add(before)

        # Kahn's algorithm for Topological sorting
        no_dependencies = [p for p in page if not dependencies[p]]
        sorted_page = []

        while no_dependencies:
            current = no_dependencies.pop()
            sorted_page.append(current)

            for p in page:
                if current in dependencies[p]:
                    dependencies[p].remove(current)
                    if not dependencies[p]:
                        no_dependencies.append(p)

        sortedPages.append(sorted_page)
        middleIndex = len(sorted_page) // 2
        middlePages.append(sorted_page[middleIndex])


    print(sum(middlePages))

sortPages(invalidPages,rules)

