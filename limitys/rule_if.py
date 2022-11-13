MAGIC_PAD = 13

ENV_KEY_SPLIT_WORDS = ('shall', 'must', 'will', 'should', 'can', 'may', 'has')
ENV_KEY_STOP_WORDS_LIST = [
    'a',
    'after',
    'and',
    'be',
    'before',
    'by',
    'exact',
    'exactly',
    'in',
    'may',
    'on',
    'of',
    'off',
    'only',
    'or',
    'select',
    'selecting',
    'shall',
    'the',
]
ENV_KEY_STOP_WORDS = tuple(sorted(ENV_KEY_STOP_WORDS_LIST + list(ENV_KEY_SPLIT_WORDS)))

ENV_KEY_SPECULATION_WORDS = (
    'familiar',
    'generally',
    'normally',
    'often',
    'rarely',
    'sufficiently',
    'traditional',
    'typically',
    'usually',
)

ENV_KEY_RE_AMBIGUOUS_WORDS = ('or', 'unless')

ENV_KEY_LINGUISTIC_AMBIGUOUS_WORDS = ('for',)

ENV_KEY_PRECEDENCE_AMBIGUOUS_COMBINATION_WORDS = (
    'a',
    'all',
    'each',
    'every',
    'most',
    'several',
    'some',
    'the',
)

ENV_KEY_ELLIPSIS_AMBIGUOUS_WORDS = ('if,', 'not,')

ENV_KEY_MULTIPLE_INDICATOR_WORDS = ('also', 'and', 'or', 'with')

ENV_KEY_VAGUE_WORDS = (  # TODO(sthagen) no stemming so brittle detection expected
    'adequate',
    'although',
    'ancillary',
    'appropriate',
    'approximately',
    'as appropriate',
    'as possible',
    'as required',
    'but',
    'common',
    'customary',
    'effective',
    'efficient',
    'except',
    'expandable',
    'extent necessary',
    'extent practical',
    'fast',
    'flexible',
    'flexible',
    'friendly',
    'generic',
    'if necessary',
    'if needed',
    'if practicable',
    'if required',
    'if so needed',
    'if so required',
    'is possible',
    'it',
    'possible',
    'proficient',
    'prove necessary',
    'readable',
    'reasonable',
    'relevant',
    'robust',
    'routine',
    'significant',
    'soon',
    'sufficient',
    'they',
    'typical',
    'unless',
    'versatile',
    'when',
    'where possible',
)

ENV_KEY_PROBABILITY_WORDS = (
    'could',
    'may',
    'might',
    'ought',
    'perhaps',
    'probably',
    'should',
    'has',
)

ENV_KEY_WISHFUL_WORDS = (
    '0%',
    '100%',
    'all',
    'always',
    'future',
    'never',
    'safe',
    'secure',
    'hide',
    'cover',
    'consider',
    'considered',
    'consideration',
    'invisible',
    'entire',
    'allow',  # TODO(shagen) in part wishful and in part soft compliance
)

ENV_KEY_USELESS_DILUTION_PHRASES = ('be able to', 'be capable of', 'the capability to')

ISSUE_KINDS: dict[str, tuple[str, ...]] = {
    'speculation': ENV_KEY_SPECULATION_WORDS,
    'requirements engineering specific ambiguity': ENV_KEY_RE_AMBIGUOUS_WORDS,
    'linguistic ambiguity': ENV_KEY_LINGUISTIC_AMBIGUOUS_WORDS,
    'precedence ambiguity upon multiple occurrence': ENV_KEY_PRECEDENCE_AMBIGUOUS_COMBINATION_WORDS,
    'ellipsis ambiguity': ENV_KEY_ELLIPSIS_AMBIGUOUS_WORDS,
    'multiple requirements': ENV_KEY_MULTIPLE_INDICATOR_WORDS,
    'vagueness': ENV_KEY_VAGUE_WORDS,
    'probability': ENV_KEY_PROBABILITY_WORDS,
    'wishful thinking': ENV_KEY_WISHFUL_WORDS,
    'useless dilution': ENV_KEY_USELESS_DILUTION_PHRASES,
}

MOTIVATION = {
    'speculation': 'Words like (usually), (generally), (often), (normally), and (typically) indicate speculation.',
    'requirements engineering specific ambiguity': (
        'An requirements engineering (RE) specific ambiguity is context dependent and can be observed only by a'
        ' reader who has knowledge of the particular requirements context or of the other requirements.'
    ),
    'linguistic ambiguity': (
        'Linguistic ambiguity is context independent and can be observed by any reader who has a tone for language.'
    ),
    'precedence ambiguity upon multiple occurrence': (
        'Scope ambiguity occurs when quantifiers, e.g., (every), (each), (all), (some), (several), (a),'
        ' and negations, e.g., (not), enter into different scope relations with the other scoped parts'
        ' of the requirements sentence. In other words, the ambiguity lies in the precedence of these operators.'
        ' Quantifiers are discussed in more detail in references.'
    ),
    'ellipsis ambiguity': (
        'Sample: If the ATM accepts the card, the user enters the PIN. If not, the card is rejected.'
        ' The word not is here an elliptical expression that refers either to the condition specified in the previous'
        ' sentence or to something written before.'
    ),
    'multiple requirements': (
        'Conjunctions like (and), (or), (with), and (also) lead to ambiguity on which parts of the requirement apply,'
        ' especially if the different clauses seem to conflict or if the individual parts apply separately.'
    ),
    'vagueness': (
        'Words and terms like (user-friendly), (wersatile), (flexible), approximately), and (as possible) indicate'
        ' vagueness. Words like (if), (when), (but), (except), (unless), and (although) may indicate escape routes'
        ' for implementations not fulfilling the requirement.'
    ),
    'probability': (
        'Words like (may), (might), (should), (ought), (could), (perhaps), and (probably) indicate expression of'
        ' possibilities (only).'
    ),
    'wishful thinking': (
        'Indicator terms indicating wishful thinking are (100%% reliable), (safe), (handle all unexpected failures),'
        ' (please all users), (run on all platforms), (never fail), and (upgradeable to all future situations)'
        ' just to name a few.'
    ),
    'useless dilution': (
        'Indicator phrases best left out as they often block any verification are (be able to) and (be capable of).'
    ),
}
