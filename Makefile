BASENAME = blockchain_slides

all: pdf

pdf::
	latexmk --pdf ${BASENAME}

ps::
	latexmk --ps ${BASENAME}

clean::
	latexmk --ps -c ${BASENAME}
	latexmk -c ${BASENAME}


