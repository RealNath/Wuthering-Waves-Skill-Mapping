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
        skill = pd.read_json('json/Skill.json')
        multiText = pd.read_json('json/MultiText.json', typ='series')
    except FileNotFoundError:
        print("Please download Skill.json and MultiText.json (EN)")
    else:
        def getValue2(jsonFile, key1, value1, key2):
            value2 = jsonFile.loc[jsonFile[key1] == value1, key2]
            if len(value2) == 1:
                return value2.values[0]
            else:
                return value2
        def mapSkill():
            #Fetch skill description
            skillDesc = multiText[textLabel]
            #Fetch skill name
            labelName = "Skill_"+str(id)+"_SkillName"
            skillName = multiText[labelName]
            #Fetch character name
            charNameID = getValue2(skill, 'Id', id, 'SkillGroupId')
            labelCharNameID = "RoleInfo_"+str(charNameID)+"_Name"
            charName = multiText[labelCharNameID]
            #Fetch skill type
            skillTypeID = getValue2(skill, 'Id', id, 'SkillType')
            labelSkillType = "SkillType_"+str(skillTypeID)+"_TypeName"
            skillType = multiText[labelSkillType]

            #merge numbers with skill description
            valueList = getValue2(skill, 'Id', id, 'SkillDetailNum')
            if valueList == None:
                pass
            else:
                for i in range(len(valueList)):
                    skillDesc = skillDesc.replace(f"{{{i}}}", valueList[i])
            
            if statusWiki:
                elements = {"<color=Highlight>":"{{Color|help|", "<color=Title>":"{{Color|menu|", "<color=Fire>":"{{Color|", "<color=Ice>":"{{Color|", "<color=Light>":"{{Color|", "<color=Thunder>":"{{Color|", "<color=Wind>":"{{Color|", "<color=Dark>":"{{Color|", "</color>":"|nobold=1}}", "<size=40>":"", "<size=10>":"", "</size>":""}
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
            print(charName+' - '+skillType+' - '+skillName+' - '+str(id))
            print("==========")
            print(skillDesc)
            print("==========\n")

        while True:
            textLabel = None
            value = input("Enter skill ID or skill/char name (add '--wiki' for Fandom Wiki format) - ").casefold()
            if " --wiki" in value:
                value = value.replace(" --wiki","")
                statusWiki = True
            else:
                statusWiki = False

            if value.isnumeric() == True:
                try:
                    id = int(value)
                    textLabel = skill.loc[skill["Id"] == id, 'SkillDescribe'].values[0]
                    mapSkill()
                except (IndexError, KeyError):
                    print("Result not found.")
            else:
                multiTextCsInsens = multiText.astype(str).apply(str.casefold)
                textLabelNames = multiTextCsInsens.iloc[np.where(multiTextCsInsens == value)].index.tolist()
                for textLabelName in textLabelNames:
                    #if value is skill name
                    if (textLabelName[:6] == 'Skill_') and (textLabelName[-10:] == '_SkillName'):
                        textLabel = textLabelName.replace("_SkillName", "_SkillDescribe")
                        id = [int(i) for i in textLabel.split('_') if i.isdigit()]
                        id = id[0]
                        mapSkill()
                        break
                    #if value is character name
                    elif (textLabelName[:9] == 'RoleInfo_') and (textLabelName[-5:] == '_Name'):
                        charID = [int(i) for i in textLabelName.split('_') if i.isdigit()]
                        charID = charID[0]
                        ids = getValue2(skill, 'SkillGroupId', charID, 'Id')
                        for id in ids:
                            try:
                                textLabel = "Skill_"+str(id)+"_SkillDescribe"
                                mapSkill()
                            except KeyError:
                                pass
                #if value not found
                if textLabel == None:
                    print("Result not found.")