try:    
    import pandas as pd
    try:
        import numpy as np
    except ImportError:
        print("NumPy library not installed.")
except ImportError:
    print("Pandas library not installed yet. Make sure NumPy is installed too.")
else:
    try:
        skill = pd.read_json('Skill.json')
        multiText = pd.read_json('MultiText.json', typ='series')
    except FileNotFoundError:
        print("Please download Skill.json and MultiText.json (EN) from WutheringData")
    else:
        def mapSkill():
            skillDesc = multiText[textLabel]
            labelName = "Skill_"+str(id)+"_SkillName"
            skillName = multiText[labelName]
            
            valueList = skill.loc[skill["Id"] == id, 'SkillDetailNum'].values[0]
            if valueList == None:
                pass
            else:
                for i in range(len(valueList)):
                    skillDesc = skillDesc.replace(f"{{{i}}}", valueList[i])
            
            if statusWiki:
                elements = {"<color=Highlight>":"{{Color|help|", "<color=Title>":"{{Color|menu|", "<color=Fire>":"", "<color=Ice>":"", "<color=Light>":"", "<color=Thunder>":"", "<color=Wind>":"", "<color=Dark>":"", "</color>":"|nobold=1}}", "<size=40>":"", "<size=10>":"", "</size>":""}
                for k, v in elements.items():
                    skillDesc = skillDesc.replace(k, v)
                #replace break lines with "<br />",break line after every "<br />",
                #then undo the break if there are 2 "<br />" next to each other
                skillDesc = skillDesc.replace("\n","<br />")
                skillDesc = skillDesc.replace("<br />", "<br /><!--\n-->")
                skillDesc = skillDesc.replace("<br /><!--\n--> <br /><!--\n-->", "<br /><br /><!--\n\n-->")
            else:
                elements = {"<color=Highlight>":"", "<color=Title>":"", "<color=Fire>":"", "<color=Ice>":"", "<color=Light>":"", "<color=Thunder>":"", "<color=Wind>":"", "<color=Dark>":"", "</color>":"", "<size=40>":"", "<size=10>":"", "</size>":""}
                for k, v in elements.items():
                    skillDesc = skillDesc.replace(k, v)

            print("\n")
            print(skillName)
            print("==========")
            print(skillDesc)
            print("==========\n")

        while True:
            textLabel = None
            value = input("Enter ID or skill name (add '--wiki' for Fandom Wiki format) - ").casefold()
            if " --wiki" in value:
                value = value.replace(" --wiki","")
                statusWiki = True
            else:
                statusWiki = False

            if value.isnumeric() == True:
                id = int(value)
                textLabel = skill.loc[skill["Id"] == id, 'SkillDescribe'].values[0]
                mapSkill()    
            else:
                multiTextCsInsens = multiText.astype(str).apply(str.casefold)
                textLabelNames = multiTextCsInsens.iloc[np.where(multiTextCsInsens == value)].index.tolist()
                for textLabelName in textLabelNames:
                    if (textLabelName[:6] == 'Skill_') and (textLabelName[-10:] == '_SkillName'):
                        textLabel = textLabelName.replace("_SkillName", "_SkillDescribe")
                        break
                if textLabel == None:
                    print("Result not found.")
                else:
                    id = [int(i) for i in textLabel.split('_') if i.isdigit()]
                    id = id[0]
                    mapSkill()