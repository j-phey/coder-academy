import '@testing-library/jest-dom'
import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import App from "../components/App";
import userEvent from '@testing-library/user-event';

describe('App Component', () => {
    let container
    // Container allows us to access the JS DOM. It's like 'document' - the name ijs arbitrary
    beforeEach(() => {
        container = render(<App />).container
    })
    
    it('Renders the Home component', () => {
        // expect(screen.getByText('Journal Entries')).toBeDefined()
        expect(container.querySelector('h3')).toHaveTextContent('Journal Entries')
    })

    it('Renders CategorySelection when Create Entry menu item is clicked', async () => {
        await userEvent.click(screen.getByText('Create Entry'))

        expect(container.querySelector('h3')).not.toBeNull()
        expect(container.querySelector('h3')).toHaveTextContent('Please select a category:')
    })
})