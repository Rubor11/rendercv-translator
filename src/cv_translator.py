from ruamel.yaml import YAML
from translator import translate_text

# yaml instance
yaml = YAML()
yaml.preserve_quotes = True

# exclude keys from translation
EXCLUDE_KEYS = ["profile", "skills"]
EXCEPTIONS = ["Soft Skills"]


# DEV ZONE -------------------------------------------------------------------

# ----------------------------------------------------------------------------
def load_yaml(path):
    # open file in read mode ('r') and close
    with open(path, 'r', encoding='utf-8') as f:
        # convert f to a py dictionary
        return yaml.load(f)

def save_yaml(data, path):
    # open file in write mode ('w') and close
    with open(path, 'w', encoding='utf-8') as f:
        # convert py dict in yaml
        yaml.dump(data, f)

def translate_dict(d, source_lan, target_lan):
    # read dict for key and value
    for k, v in d.items():
        # # exclusion keys
        # if k in EXCLUDE_KEYS:
        #     # exception subkeys
        #     if isinstance(v, dict):
        #         for subkey, subval in v.items():
        #             if subkey in EXCEPTIONS and isinstance(subval, str):
        #                 v[subkey] = translate_text(subval, source_lan, target_lan)
        #     elif isinstance(v, list):
        #         for item in v:
        #             if isinstance(item, dict):
        #                 for subkey, subval in item.items():
        #                     if subkey in EXCEPTIONS and isinstance(subval, str):
        #                         item[subkey] = translate_text(subval, source_lan, target_lan)
        #     continue  
        # translate simple string values
        if isinstance(v, str):
            d[k] = translate_text(v, source_lan, target_lan)
        # translate nested dict values
        elif isinstance(v, dict):
           translate_dict(v, source_lan, target_lan)
        # translate list values
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, str):
                    v[i] = translate_text(item, source_lan, target_lan)
                elif isinstance(item, dict):
                    translate_dict(item, source_lan, target_lan)
    # return dict translated
    return d

def main():
    path = input("Insert CV absolut path: ")
    if not (path):
        path = "C:/Users/sistemas4/OneDrive - Soho Boutique Hotels/Escritorio/Rubor/rendercv-translator/cv/curriculum.yaml"
    cv_data = load_yaml(path)

    source_lan = input("Source CV language (default: en): ") or "en"
    target_lan = input("Target language: ")

    translated_cv = translate_dict(cv_data, source_lan, target_lan)
    created_file = path.replace(".yaml", f"_{target_lan}.yaml")
    save_yaml(translated_cv, created_file)

    print(f"Translated CV saved in: {created_file}")

if __name__ == "__main__":
    main()

