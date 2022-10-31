import random


def predict_marital(age, gender, seed):
    """
    Predict marital status based on age and gender
    Source: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710006001
    """
    random.seed(seed)
    p = random.uniform(0, 1)
    re = "divorced"
    if 20 <= age <= 24:  # age from 20 to 24
        if gender == "F":  # female
            if p < 1117789 / 1182769:
                re = "single"
            elif p < (1117789 + 57769) / 1182769:
                re = "married"
            elif p < (1117789 + 57769 + 3766) / 1182769:
                re = "separated"
            elif p < (1117789 + 57769 + 3766 + 1345) / 1182769:
                re = "widowed"
            else:
                re = "divorced"
        else:  # male
            if p < 1257587 / 1292734:
                re = "single"
            elif p < (1257587 + 28379) / 1292734:
                re = "married"
            elif p < (1257587 + 28379 + 2714) / 1292734:
                re = "separated"
            elif p < (1257587 + 28379 + 2714 + 2538) / 1292734:
                re = "widowed"
            else:
                re = "divorced"
    elif 25 <= age <= 29:  # age from 25 to 29
        if gender == "F":  # female
            if p < 924113 / 1272298:
                re = "single"  # single
            elif p < (924113 + 313994) / 1272298:
                re = "married"
            elif p < (924113 + 313994 + 17927) / 1272298:
                re = "separated"
            elif p < (924113 + 313994 + 17927 + 2418) / 1272298:
                re = "widowed"
            else:
                re = "divorced"
        else:  # male
            if p < 1121401 / 1353906:
                re = "single"  # single
            elif p < (1121401 + 207666) / 1353906:
                re = "married"
            elif p < (1121401 + 207666 + 12391) / 1353906:
                re = "separated"
            elif p < (1121401 + 207666 + 12391 + 3469) / 1353906:
                re = "widowed"
            else:
                re = "divorced"
    elif 30 <= age <= 34:  # age from 30 to 34
        if gender == "F":  # female
            if p < 604542 / 1286054:
                re = "single"  # single
            elif p < (604542 + 598041) / 1286054:
                re = "married"
            elif p < (604542 + 598041 + 40936) / 1286054:
                re = "separated"
            elif p < (604542 + 598041 + 40936 + 3042) / 1286054:
                re = "widowed"
            else:
                re = "divorced"
        else:  # male
            if p < 754938 / 1319340:
                re = "single"  # single
            elif p < (754938 + 500441) / 1319340:
                re = "married"
            elif p < (754938 + 500441 + 31255) / 1319340:
                re = "separated"
            elif p < (754938 + 500441 + 31255 + 2744) / 1319340:
                re = "widowed"
            else:
                re = "divorced"
    elif 35 <= age <= 39:  # age from 35 to 39
        if gender == "F":  # female
            if p < 445219 / 1292320:
                re = "single"  # single
            elif p < (445219 + 705048) / 1292320:
                re = "married"
            elif p < (445219 + 705048 + 61145) / 1292320:
                re = "separated"
            elif p < (445219 + 705048 + 61145 + 5336) / 1292320:
                re = "widowed"
            else:
                re = "divorced"
        else:  # male
            if p < 529826 / 1288726:
                re = "single"  # single
            elif p < (529826 + 651741) / 1288726:
                re = "married"
            elif p < (529826 + 651741 + 48041) / 1288726:
                re = "separated"
            elif p < (529826 + 651741 + 48041 + 3104) / 1288726:
                re = "widowed"
            else:
                re = "divorced"
    elif 40 <= age <= 44:  # age from 40 to 44
        if gender == "F":  # female
            if p < 328034 / 1223242:
                re = "single"  # single
            elif p < (328034 + 699232) / 1223242:
                re = "married"
            elif p < (328034 + 699232 + 70576) / 1223242:
                re = "separated"
            elif p < (328034 + 699232 + 70576 + 10055) / 1223242:
                re = "widowed"
            else:
                re = "divorced"
        else:  # male
            if p < 383018 / 1198647:
                re = "single"  # single
            elif p < (383018 + 670806) / 1198647:
                re = "married"
            elif p < (383018 + 670806 + 56144) / 1198647:
                re = "separated"
            elif p < (383018 + 670806 + 56144 + 4379) / 1198647:
                re = "widowed"
            else:
                re = "divorced"
    elif 45 <= age <= 49:  # age from 45 to 49
        if gender == "F":  # female
            if p < 265137 / 1207157:
                re = "single"  # single
            elif p < (265137 + 694744) / 1207157:
                re = "married"
            elif p < (265137 + 694744 + 70795) / 1207157:
                re = "separated"
            elif p < (265137 + 694744 + 70795 + 18917) / 1207157:
                re = "widowed"
            else:
                re = "divorced"
        else:  # male
            if p < 325079 / 1191221:
                re = "single"  # single
            elif p < (325079 + 679455) / 1191221:
                re = "married"
            elif p < (325079 + 679455 + 62802) / 1191221:
                re = "separated"
            elif p < (325079 + 679455 + 62802 + 7435) / 1191221:
                re = "widowed"
            else:
                re = "divorced"
    else:  # age from 50 to 54
        if gender == "F":  # female
            if p < 232672 / 1258000:
                re = "single"  # single
            elif p < (232672 + 724298) / 1258000:
                re = "married"
            elif p < (232672 + 724298 + 67135) / 1258000:
                re = "separated"
            elif p < (232672 + 724298 + 67135 + 34441) / 1258000:
                re = "widowed"
            else:
                re = "divorced"
        else:  # male
            if p < 302359 / 1247044:
                re = "single"  # single
            elif p < (302359 + 710188) / 1247044:
                re = "married"
            elif p < (302359 + 710188 + 64533) / 1247044:
                re = "separated"
            elif p < (302359 + 710188 + 64533 + 13077) / 1247044:
                re = "widowed"
            else:
                re = "divorced"
    return re


def predict_education(age, gender, seed):
    """
    Predict the education level based on age and gender.
    Source: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3710013001
    """
    random.seed(seed)
    p = random.uniform(0, 1)
    re = "tertiary education"
    if 20 <= age <= 34:  # age from 20 to 34
        if gender == "F":  # female
            if p < 0.05:
                re = "below upper secondary"
            elif p < 0.05 + 0.24:
                re = "upper secondary and post-secondary non-tertiary"
            else:
                re = "tertiary education"
        else:  # male
            if p < 0.07:
                re = "below upper secondary"
            elif p < 0.07 + 0.38:
                re = "upper secondary and post-secondary non-tertiary"
            else:
                re = "tertiary education"
    elif 35 <= age <= 44:  # age from 35 to 44
        if gender == "F":
            if p < 0.05:
                re = "below upper secondary"
            elif p < 0.05 + 0.24:
                re = "upper secondary and post-secondary non-tertiary"
            else:
                re = "tertiary education"
        else:
            if p < 0.07:
                re = "below upper secondary"
            elif p < 0.07 + 0.36:
                re = "upper secondary and post-secondary non-tertiary"
            else:
                re = "tertiary education"
    else:  # age from 45 to 54
        if gender == "F":
            if p < 0.07:
                re = "below upper secondary"
            elif p < 0.07 + 0.28:
                re = "upper secondary and post-secondary non-tertiary"
            else:
                re = "tertiary education"
        else:
            if p < 0.09:
                re = "below upper secondary"
            elif p < 0.09 + 0.36:
                re = "upper secondary and post-secondary non-tertiary"
            else:
                re = "tertiary education"
    return re


def predict_min_offer(income, p):
    """
    Predict minimal offer value based on income
    The ratio of minimal offer value / income = p
    """
    return max(income * (p + 1) / 1000, 0)
