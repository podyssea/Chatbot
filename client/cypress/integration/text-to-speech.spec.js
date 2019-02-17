describe('Text-to-speech is enabled and disabled correctly', function () {
    beforeEach(function () {
       cy.visit('http://localhost:3000');
       cy.get('.rsc-float-button').click();
    });

    it('Bot recognises text-to-speech enabling prompt and acts accordingly', function () {
        cy.get('.rsc-content').should('be.visible');
    });

    it('Bot recognises text-to-speech disabling prompt and acts accordingly', function () {
    });

});